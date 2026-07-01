from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.database.models.approval import ApprovalRequest


def create_approval(state):

    db: Session = SessionLocal()

    approval = ApprovalRequest(
        session_id=state["session_id"],
        question=state["question"],
        answer=state["final_answer"],
        confidence_score=str(state["confidence_score"]),
    )

    db.add(approval)
    db.commit()
    db.refresh(approval)

    db.close()

    return approval.id