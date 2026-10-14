import uuid

from dotenv import load_dotenv
from src.graph import graph

load_dotenv()

# Create an ID for this conversation
thread_id = str(uuid.uuid4())

# Information given to the graph
config = {
    "configurable": {
        "passenger_id": "3442 587242",
        "thread_id": thread_id,
    }
}

# Ask the user questions
questions = [
    "Hi there, what time is my flight?",
    "Am I allowed to update my flight to something sooner?",
    "Update my flight to sometime next week then",
    "The next available option is great",
]

# Send each question to the graph
for question in questions:

    events = graph.stream(
        {"messages": ("user", question)},
        config
    )

    # Print the graph's responses
    for event in events:
        print(event)

    # Check if graph is waiting for approval
    snapshot = graph.get_state(config)

    while snapshot.next:

        user_input = input("Do you approve? Type y to continue: ")

        if user_input == "y":
            # Continue from where the graph stopped
            graph.invoke(None, config)

        snapshot = graph.get_state(config)