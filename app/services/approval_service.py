from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.database.models.approval import ApprovalRequest
from app.observability.logger import logger


def create_approval(state):
    try:
        db: Session = SessionLocal()

        approval = ApprovalRequest(
            session_id=state["session_id"],
            question=state["question"],
            answer=state.get("final_answer", ""),
            confidence_score=str(state.get("confidence_score", 0.0)),
        )

        db.add(approval)
        db.commit()
        db.refresh(approval)
        db.close()

        return approval.id
    except Exception as error:
        logger.warning(f"Approval persistence failed: {error}")
        return None