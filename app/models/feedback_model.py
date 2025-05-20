# backend/app/models/feedback_model.py

from pydantic import BaseModel

class Feedback(BaseModel):
    event_id: str
    user: str
    feedback_text: str
