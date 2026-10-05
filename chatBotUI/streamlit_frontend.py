import streamlit as st

from langgraphUI import chatbot
from langchain_core.messages import HumanMessage


# Initialize session state
if 'message_hist' not in st.session_state:
    st.session_state['message_hist'] = []


# Display previous messages
for message in st.session_state['message_hist']:
    with st.chat_message(message['role']):
        st.text(message['content'])


# Get user input
user_input = st.chat_input('Type here')


if user_input:

    # Store user message
    st.session_state['message_hist'].append({
        'role': 'user',
        'content': user_input
    })

    # Display user message
    with st.chat_message('user'):
        st.text(user_input)

    # Invoke LangGraph
    # response = chatbot.invoke(
    #     {
    #         'messages': [
    #             HumanMessage(content=user_input)
    #         ]
    #     },
    #     config={
    #         'configurable': {
    #             'thread_id': 'user_1'
    #         }
    #     }
    # )

    # Get AI response
    # ai_message = response['messages'][-1].content

    # Store AI response
    

    # Display AI response
    with st.chat_message('assistant'):

        ai_message = st.write_stream(
           message_chunk.content for message_chunk, metadata in  chatbot.stream(
                {
                            'messages': [
                                HumanMessage(content=user_input)
                            ]
                        },
                        config={
                            'configurable': {
                                'thread_id': 'user_1'
                            }
                        },
                        stream_mode='messages'
            )


        )
        st.session_state['message_hist'].append({
                'role': 'assistant',
                'content': ai_message
            })