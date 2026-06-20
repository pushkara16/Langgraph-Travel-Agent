from langchain_core.messages import HumanMessage
from your_graph_file import graph  # change to your actual filename

def run():
    # initial state
    state = {
        "messages": [HumanMessage(content="Hi, I want to book a flight")],
        "user_info": "",
        "dialog_state": [],
    }

    config = {"configurable": {"thread_id": "1"}}

    result = graph.invoke(state, config=config)

    print("\nFinal Output:\n")
    for msg in result["messages"]:
        print(msg)


if __name__ == "__main__":
    run()