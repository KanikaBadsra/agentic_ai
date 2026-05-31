from datetime import datetime
from app.mcp.filesystem_tool import save_report
from app.observability.timer import track_time
from app.utils.tracing import add_trace
from app.utils.timer import (
    start_timer,
    end_timer
)

@track_time("Report Node")
def report_node(state):
    timer = start_timer()

    state["active_agent"] = "report_agent"

    add_trace(
        state,
        "Report Node Started"
    )
    question = state["question"]

    final_answer = state["final_answer"]

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"sales_report_{timestamp}.txt"

    report_content = f"""
Question:
{question}


AI Analysis:
{final_answer}
"""

    saved_path = save_report(
        filename,
        report_content
    )
    duration = end_timer(timer)

    add_trace(
        state,
        f"Report Node Completed ({duration}s)"
    )
    return {
        "report_path": saved_path
    }