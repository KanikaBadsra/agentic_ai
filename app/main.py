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
        #return result
        return {
    "answer": result.get("final_answer", ""),
    "trace": result["execution_trace"],
    "risk_level": result["risk_level"],

    "requires_review": result["requires_human_review"],

    "trace": result["execution_trace"]
}

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    