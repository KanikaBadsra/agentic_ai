from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.graphs.main_graph import graph
import time
from app.observability.logger import logger
from app.memory.conversation_memory import save_message
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from jose import jwt
from fastapi.security import HTTPBearer
from app.auth.auth import get_current_user, verify_token, create_access_token
security = HTTPBearer()
app = FastAPI()

limiter = Limiter(
    key_func=get_remote_address
)
app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    lambda request, exc: JSONResponse(
        status_code=429,
        content={
            "detail": "Rate limit exceeded"
        }
    )
)

app.add_middleware(
    SlowAPIMiddleware
)

class ChatRequest(BaseModel):
    question: str
    session_id: str


@app.get("/")
def home():
    return {"message": "NexusIQ Running"}

@app.post("/login")
def login():

    token = create_access_token(
        username="admin",
        role="Admin"
    )

    return {
        "access_token": token
    }

@app.post("/chat")
@limiter.limit("10/minute")
def chat(request: Request,
    body: ChatRequest,
    user = Depends(get_current_user)):

    try:

        start_time = time.time()
        result = graph.invoke({
            "question": body.question,
            "session_id": body.session_id,
            "user_role": user["role"]
        })
         # SAVE USER MESSAGE
        save_message(
            body.session_id,
            "user",
            body.question
        )
        logger.info(f"Graph Result: {result}")
        # SAVE ASSISTANT RESPONSE
        save_message(
            body.session_id,
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
        final_answer = result.get("final_answer", "")
        guardrail_status = result.get("guardrail_status") or ("PASSED" if final_answer else "BLOCKED")

        return {
            "answer": final_answer,
            "confidence_score": result.get("confidence_score", 0.0),
            "risk_level": result.get("risk_level", "HIGH"),
            "requires_human_review": result.get("requires_human_review", True),
            "guardrail_status": guardrail_status,
            "approval_id": result.get("approval_id")
        }
    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    