import shutil
import uuid

from langchain_core.messages import ToolMessage

from src.graph import graph
from src.utils.database import LOCAL_FILE, download_database, update_dates
from src.utils.utilities import _print_event


update_dates()
thread_id = str(uuid.uuid4())
     

config = {
    "configurable": {
        "passenger_id": "3442 587242",
        "thread_id": str(uuid.uuid4()),
    }
}

query = input("User: ")

graph.stream(
    {"messages": [("user", query)]},
    config,
)

snapshot = graph.get_state(config)

if snapshot.next:
    print("Agent wants to perform an action.")

    approval = input("Approve? (y/n): ")

    if approval.lower() == "y":

        # resume graph
        graph.invoke(None, config)

    else:

        graph.invoke(
            {
                "messages": [
                    ToolMessage(
                        tool_call_id="tool_id_here",
                        content="User rejected action."
                    )
                ]
            },
            config,
        )
