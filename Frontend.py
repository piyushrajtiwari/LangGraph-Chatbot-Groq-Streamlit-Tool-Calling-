import streamlit as st
from Backend import workflow,retrieve_all_threads
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
from uuid import uuid4


# utilts

def thread_id():
    return str(uuid4())

def new_chat():
    st.session_state['tread_id'] =thread_id()
    tread_history(st.session_state['tread_id'])  
    st.session_state['message_history'] = []

def tread_history(tread_id):
    if tread_id not in st.session_state['tread_history']:
        st.session_state['tread_history'].append(tread_id)

def conversation(tread_id):
    config = {"configurable": {"thread_id": tread_id}}
    state = workflow.get_state(config=config)
    return state.values.get("messages", [])


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'tread_id' not in st.session_state:
    st.session_state['tread_id'] = thread_id()

if 'tread_history' not in st.session_state:
    st.session_state['tread_history'] = retrieve_all_threads()
    
tread_history(st.session_state['tread_id'])   
    
st.sidebar.title('CHATBOT')
if st.sidebar.button('ADD'):
    new_chat()
    
st.sidebar.header('CONVERSATION')

for tread in st.session_state['tread_history'][::-1]:
    if st.sidebar.button(tread):
        st.session_state['tread_id'] = tread
        message = conversation(tread)
        
        message_history = []
        for msg in message:
            if isinstance(msg,HumanMessage):
                role = 'user'
            else:
                role = 'ai'
            message_history.append({'role':role,'content':msg.content})
        st.session_state['message_history'] = message_history
    
for msg in st.session_state['message_history']:
    with st.chat_message(msg['role']):
        st.text(msg['content'])


input_user = st.chat_input()

if input_user:
    st.session_state['message_history'].append({'role':'user','content':input_user})
    with st.chat_message('user'):
        st.text(input_user)
    
    config = {"configurable": {"thread_id": st.session_state['tread_id']}}
    
    status_holder ={'box':None}
    with st.chat_message('ai'):
        def streaming():
            for message_chunk, metadata in workflow.stream(
            {'messages':[HumanMessage(content=input_user)]},
            stream_mode="messages",
            config=config
        ):

                # Lazily create & update the SAME status container when any tool runs
                if isinstance(message_chunk, ToolMessage):
                    tool_name = getattr(message_chunk, "name", "tool")
                    if status_holder["box"] is None:
                        status_holder["box"] = st.status(
                            f"🔧 Using `{tool_name}` …", expanded=True
                        )
                    else:
                        status_holder["box"].update(
                            label=f"🔧 Using `{tool_name}` …",
                            state="running",
                            expanded=True,
                        )

                # Stream ONLY assistant tokens
                if isinstance(message_chunk, AIMessage):
                    yield message_chunk.content

        ai_message = st.write_stream(streaming())

        # Finalize only if a tool was actually used
        if status_holder["box"] is not None:
            status_holder["box"].update(
                label="✅ Tool finished", state="complete", expanded=False
            )

        

    st.session_state['message_history'].append({'role':'ai','content':ai_message})
    
