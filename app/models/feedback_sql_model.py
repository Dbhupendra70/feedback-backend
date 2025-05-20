from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class FeedbackDB(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(String)
    user = Column(String)
    feedback_text = Column(String)
    sentiment = Column(String)
    score = Column(Float)
