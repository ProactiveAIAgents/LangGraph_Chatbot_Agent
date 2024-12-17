import os
from typing import Annotated

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatAnthropic(temperature=0.7, model="claude-3-opus-20240229")

# Create a prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant."),
        ("human", "{input}"),
    ]
)


class ChatState(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot_agent(state: ChatState):
    # Get the last message
    last_message = state["messages"][-1]

    # Format the prompt with the input
    chain = prompt | llm

    # Generate response
    response = chain.invoke({"input": last_message.content})

    return {"messages": [(response.content)]}


# Create the graph
chat_graph = StateGraph(ChatState)

# Add nodes and edges
chat_graph.add_node("chatbot_agent", chatbot_agent)
chat_graph.add_edge(START, "chatbot_agent")
chat_graph.add_edge("chatbot_agent", END)

# Compile the graph
graph_app = chat_graph.compile()


def stream_graph_updates(user_input: str):
    for event in graph_app.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1])


if __name__ == "__main__":
    print("Chat with AI Assistant (type 'quit' to exit)")
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Thank you and Goodbye!")
                break

            stream_graph_updates(user_input)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

print(os.getenv("ANTHROPIC_API_KEY"))
