from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.graphs.main_graph import graph
import time
from app.observability.logger import logger
from app.memory.conversation_memory import save_message
app = FastAPI()


class ChatRequest(BaseModel):
    question: str
    session_id: str


@app.get("/")
def home():
    return {"message": "NexusIQ Running"}


@app.post("/chat")
def chat(request: ChatRequest):

    try:

        start_time = time.time()
        result = graph.invoke({
            "question": request.question,
            "session_id": request.session_id
        })
         # SAVE USER MESSAGE
        save_message(
            request.session_id,
            "user",
            request.question
        )
        logger.info(f"Graph Result: {result}")
        # SAVE ASSISTANT RESPONSE
        save_message(
            request.session_id,
            "assistant",
            result.get("final_answer", "")
        )
        end_time = time.time()

        execution_time = round(
            end_time - start_time,
            2
        )

        logger.info(
            f"Execution time: {execution_time} sec"
        )

        # return {
        #     "answer": result.get("final_answer", ""),
        #     "trace": result.get("execution_trace", []),
        #     "risk_level": result.get("risk_level", "UNKNOWN"),
        #     "requires_review": result.get("requires_human_review", True)
        # }
        return {
        "answer": result["final_answer"],
        "confidence_score":
            result.get("confidence_score"),
        "risk_level":
            result.get("risk_level"),
        "requires_human_review":
            result.get("requires_human_review"),
        "guardrail_status":
            result.get("guardrail_status")
    }
    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    