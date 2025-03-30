import pytest
from fastapi.testclient import TestClient
from datetime import datetime, timedelta
from app.main import app
from app.models import Message

client = TestClient(app)

@pytest.fixture
def sample_messages():
    return [
        Message(
            content="Olá, tudo bem? 😊",
            sender="contact",
            timestamp=datetime.now() - timedelta(minutes=10)
        ),
        Message(
            content="Oi! Tudo ótimo, e você?",
            sender="user",
            timestamp=datetime.now() - timedelta(minutes=9)
        ),
        Message(
            content="Estou bem também! Que bom te ver por aqui 😄",
            sender="contact",
            timestamp=datetime.now() - timedelta(minutes=8)
        )
    ]

def test_analyze_conversation(sample_messages):
    response = client.post(
        "/conversations/analyze",
        json=[msg.dict() for msg in sample_messages]
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "formality_level" in data
    assert "response_time_avg" in data
    assert "emoji_usage" in data
    assert "message_length_avg" in data
    assert "sentiment_avg" in data

def test_generate_response():
    conversation_context = {
        "formality_level": 0.7,
        "sentiment_avg": 0.8,
        "last_message": "Olá, como posso ajudar?"
    }
    
    response = client.post(
        "/conversations/generate-response",
        json=conversation_context
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert isinstance(data["response"], str)
    assert len(data["response"]) > 0

def test_summarize_conversation(sample_messages):
    response = client.post(
        "/conversations/summarize",
        json=[msg.dict() for msg in sample_messages]
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert "key_points" in data
    assert "next_actions" in data
    assert isinstance(data["key_points"], list)
    assert isinstance(data["next_actions"], list)

def test_get_conversation_priority():
    response = client.get("/conversations/1/priority")
    
    assert response.status_code == 200
    data = response.json()
    assert "priority" in data
    assert isinstance(data["priority"], int)
    assert 0 <= data["priority"] <= 5

def test_get_conversation_pattern():
    response = client.get("/conversations/1/pattern")
    
    assert response.status_code == 200
    data = response.json()
    assert "formality_level" in data
    assert "response_time_avg" in data
    assert "emoji_usage" in data
    assert "message_length_avg" in data
    assert "sentiment_avg" in data
    assert 0 <= data["formality_level"] <= 1
    assert 0 <= data["emoji_usage"] <= 1
    assert -1 <= data["sentiment_avg"] <= 1 