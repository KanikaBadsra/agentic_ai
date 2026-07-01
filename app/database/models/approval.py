from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database.connection import Base

class ApprovalRequest(Base):
    __tablename__ = "approval_requests"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(String)

    question = Column(Text)

    answer = Column(Text)

    confidence_score = Column(String)

    status = Column(String, default="PENDING")

    approved_by = Column(String, nullable=True)

    approved_at = Column(DateTime(timezone=True), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())