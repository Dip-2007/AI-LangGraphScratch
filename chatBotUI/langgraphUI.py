from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import HumanMessage,BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import MemorySaver


from langgraph.graph.message import add_messages

from dotenv import load_dotenv
load_dotenv()

class ChatState(TypedDict):
  messages : Annotated[list[BaseMessage],add_messages]
  


llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

def chat_node(state: ChatState):
  messages= state['messages']

  response = llm.invoke(messages)

  return{'messages': [response]}

memory = MemorySaver()

graph = StateGraph(ChatState)

graph.add_node('chat_node',chat_node)


graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer=memory)

# while True:
#     user_message = input("You: ")
#     print(f"You: {user_message}")

#     if user_message.lower() == "exit":
#         break

#     response = chatbot.invoke(
#         {
#             "messages": [
#                 ("user", user_message)
#             ]
#         },
#         config={
#             "configurable": {
#                 "thread_id": "user_1"
#             }
#         }
#     )

#     print("Bot:", response["messages"][-1].content)