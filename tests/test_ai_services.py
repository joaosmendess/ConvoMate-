import pytest
from datetime import datetime, timedelta
from app.ai_services import AIService

@pytest.fixture
def ai_service():
    return AIService()

@pytest.fixture
def sample_messages():
    return [
        {
            "content": "Olá, tudo bem? 😊",
            "sender": "contact",
            "timestamp": datetime.now() - timedelta(minutes=10)
        },
        {
            "content": "Oi! Tudo ótimo, e você?",
            "sender": "user",
            "timestamp": datetime.now() - timedelta(minutes=9)
        },
        {
            "content": "Estou bem também! Que bom te ver por aqui 😄",
            "sender": "contact",
            "timestamp": datetime.now() - timedelta(minutes=8)
        }
    ]

@pytest.mark.asyncio
async def test_analyze_conversation_pattern(ai_service, sample_messages):
    pattern = await ai_service.analyze_conversation_pattern(sample_messages)
    
    assert isinstance(pattern, dict)
    assert "formality_level" in pattern
    assert "response_time_avg" in pattern
    assert "emoji_usage" in pattern
    assert "message_length_avg" in pattern
    assert "sentiment_avg" in pattern

@pytest.mark.asyncio
async def test_generate_response(ai_service):
    conversation_context = {
        "formality_level": 0.7,
        "sentiment_avg": 0.8,
        "last_message": "Olá, como posso ajudar?"
    }
    
    response = await ai_service.generate_response(conversation_context)
    
    assert isinstance(response, str)
    assert len(response) > 0

@pytest.mark.asyncio
async def test_generate_summary(ai_service, sample_messages):
    summary = await ai_service.generate_summary(sample_messages)
    
    assert isinstance(summary, dict)
    assert "summary" in summary
    assert "key_points" in summary
    assert "next_actions" in summary
    assert isinstance(summary["key_points"], list)
    assert isinstance(summary["next_actions"], list)

@pytest.mark.asyncio
async def test_analyze_message(ai_service):
    message = "Olá, tudo bem? 😊"
    analysis = await ai_service._analyze_message(message)
    
    assert isinstance(analysis, dict)
    assert "formality" in analysis
    assert "sentiment" in analysis
    assert 0 <= analysis["formality"] <= 1
    assert -1 <= analysis["sentiment"] <= 1 