from typing import TypedDict,Annotated
from langgraph.graph import StateGraph,START,END
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from dotenv import load_dotenv
# from langgraph.checkpoint.memory import MemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode,tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
import sqlite3

import os

#loading all env
load_dotenv()

# loading model here
model = ChatGroq(
    # model="llama-3.1-8b-instant", ---> it for Rag
    model= "qwen/qwen3-32b",
    api_key=os.environ["GROQ_API_KEY"]
)

#Creating State
class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage],add_messages]

search = DuckDuckGoSearchRun()
tools = [search]
model_tools = model.bind_tools(tools)

#make Node
def chat_node(state:ChatState):
    response = model_tools.invoke(state["messages"])
    
    return {'messages':[response]}




tool_node = ToolNode(tools)
graph = StateGraph(ChatState)

graph.add_node('chat_node',chat_node)
graph.add_node('tools',tool_node)

graph.add_edge(START,'chat_node')
graph.add_conditional_edges('chat_node',tools_condition)
graph.add_edge('tools','chat_node')

conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)

checkpointer = SqliteSaver(conn=conn)
# checkpointer = MemorySaver()
workflow = graph.compile(checkpointer=checkpointer)


def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)

