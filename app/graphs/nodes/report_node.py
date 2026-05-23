from datetime import datetime
from app.mcp.filesystem_tool import save_report
from app.observability.timer import track_time


@track_time("Report Node")
def report_node(state):

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

    return {
        "report_path": saved_path
    }