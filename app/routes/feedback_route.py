from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from textblob import TextBlob
from app.models.feedback_model import Feedback
from app.models.feedback_sql_model import FeedbackDB
from app.deps import get_db

router = APIRouter()

@router.post("/")
def submit_feedback(feedback: Feedback, db: Session = Depends(get_db)):
    analysis = TextBlob(feedback.feedback_text)
    score = analysis.sentiment.polarity

    sentiment = (
        "Positive" if score > 0
        else "Negative" if score < 0
        else "Neutral"
    )

    new_feedback = FeedbackDB(
        event_id=feedback.event_id,
        user=feedback.user,
        feedback_text=feedback.feedback_text,
        sentiment=sentiment,
        score=score
    )

    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return {
        "id": new_feedback.id,
        "event_id": new_feedback.event_id,
        "user": new_feedback.user,
        "sentiment": new_feedback.sentiment,
        "score": new_feedback.score
    }

@router.get("/")
def get_feedbacks(db: Session = Depends(get_db)):
    return db.query(FeedbackDB).all()

@router.get("/")
def welcome():
    return {
        "message": "Welcome to the Sentiment-Driven Feedback API 👋",
        "available_routes": ["/api/feedback", "/api/users"]
    }

   
# @router.get("/{event_id}")
# def get_feedback_by_event(event_id: int):
#     feedbacks = load_feedbacks()
#     event_feedbacks = [feedback for feedback in feedbacks if feedback["event_id"] == event_id]
#     return event_feedbacks