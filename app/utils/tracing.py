from datetime import datetime


def add_trace(state, message):

    timestamp = datetime.now().strftime(
        "%H:%M:%S"
    )

    trace_message = f"[{timestamp}] {message}"

    if "execution_trace" not in state:
        state["execution_trace"] = []

    state["execution_trace"].append(
        trace_message
    )

    return state