from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    id: Optional[int] = None
    email: str
    name: str
    created_at: datetime = datetime.now()
    is_active: bool = True

class Conversation(BaseModel):
    id: Optional[int] = None
    user_id: int
    contact_name: str
    platform: str  # whatsapp, email, etc
    last_message: str
    last_message_time: datetime
    priority: int = 0  # 0-5, onde 5 é mais urgente
    conversation_pattern: Optional[dict] = None
    created_at: datetime = datetime.now()

class Message(BaseModel):
    id: Optional[int] = None
    conversation_id: int
    content: str
    sender: str  # user ou contact
    timestamp: datetime
    sentiment: Optional[float] = None
    formality: Optional[float] = None
    urgency: Optional[float] = None

class ConversationSummary(BaseModel):
    conversation_id: int
    summary: str
    key_points: List[str]
    next_actions: List[str]
    generated_at: datetime = datetime.now()

class ConversationPattern(BaseModel):
    conversation_id: int
    formality_level: float  # 0-1
    response_time_avg: float
    emoji_usage: float  # 0-1
    message_length_avg: float
    sentiment_avg: float
    last_updated: datetime = datetime.now() 