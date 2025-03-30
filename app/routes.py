from fastapi import APIRouter, HTTPException, Depends
from typing import List
from .models import User, Conversation, Message, ConversationSummary, ConversationPattern
from .ai_services import AIService

router = APIRouter()
ai_service = AIService()

@router.post("/conversations/analyze")
async def analyze_conversation(messages: List[Message]):
    """Analisa o padrão de uma conversa"""
    try:
        pattern = await ai_service.analyze_conversation_pattern(messages)
        return pattern
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/conversations/generate-response")
async def generate_response(conversation_context: dict):
    """Gera uma resposta apropriada para a conversa"""
    try:
        response = await ai_service.generate_response(conversation_context)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/conversations/summarize")
async def summarize_conversation(messages: List[Message]):
    """Gera um resumo da conversa"""
    try:
        summary = await ai_service.generate_summary(messages)
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/conversations/{conversation_id}/priority")
async def get_conversation_priority(conversation_id: int):
    """Calcula a prioridade de uma conversa"""
    try:
        # Aqui você implementaria a lógica para calcular a prioridade
        # baseada em fatores como tempo de resposta, urgência das mensagens, etc.
        return {"priority": 3}  # Exemplo
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/conversations/{conversation_id}/pattern")
async def get_conversation_pattern(conversation_id: int):
    """Retorna o padrão de conversa identificado"""
    try:
        # Aqui você implementaria a lógica para recuperar o padrão
        # armazenado para uma conversa específica
        return {
            "formality_level": 0.7,
            "response_time_avg": 300,
            "emoji_usage": 0.3,
            "message_length_avg": 50,
            "sentiment_avg": 0.5
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 