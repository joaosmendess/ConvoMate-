from openai import OpenAI
import numpy as np
from typing import List, Dict
import os
from datetime import datetime

class AIService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    async def analyze_conversation_pattern(self, messages: List[Dict]) -> Dict:
        """Analisa o padrão de conversa baseado nas mensagens"""
        # Extrai características das mensagens
        formality_scores = []
        response_times = []
        emoji_counts = []
        message_lengths = []
        sentiments = []
        
        for i in range(1, len(messages)):
            # Calcula tempo de resposta
            time_diff = (messages[i]["timestamp"] - messages[i-1]["timestamp"]).total_seconds()
            response_times.append(time_diff)
            
            # Analisa formalidade e sentimento usando OpenAI
            analysis = await self._analyze_message(messages[i]["content"])
            formality_scores.append(analysis["formality"])
            sentiments.append(analysis["sentiment"])
            
            # Conta emojis
            emoji_count = sum(1 for char in messages[i]["content"] if char in "😀😃😄😁😅😂🤣😊😇🙂🙃😉😌😍🥰")
            emoji_counts.append(emoji_count)
            
            message_lengths.append(len(messages[i]["content"]))
        
        return {
            "formality_level": np.mean(formality_scores),
            "response_time_avg": np.mean(response_times),
            "emoji_usage": np.mean(emoji_counts) / 10,  # Normalizado
            "message_length_avg": np.mean(message_lengths),
            "sentiment_avg": np.mean(sentiments)
        }
    
    async def generate_response(self, conversation_context: Dict) -> str:
        """Gera uma resposta apropriada baseada no contexto da conversa"""
        prompt = f"""
        Contexto da conversa:
        - Padrão de formalidade: {conversation_context['formality_level']}
        - Sentimento médio: {conversation_context['sentiment_avg']}
        - Última mensagem: {conversation_context['last_message']}
        
        Gere uma resposta apropriada que mantenha o mesmo nível de formalidade e tom emocional.
        """
        
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        
        return response.choices[0].message.content
    
    async def generate_summary(self, messages: List[Dict]) -> Dict:
        """Gera um resumo da conversa com pontos principais e próximas ações"""
        messages_text = "\n".join([f"{m['sender']}: {m['content']}" for m in messages])
        
        prompt = f"""
        Analise a seguinte conversa e forneça:
        1. Um resumo conciso
        2. Pontos principais discutidos
        3. Próximas ações necessárias
        
        Conversa:
        {messages_text}
        """
        
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        
        # Processa a resposta para extrair as seções
        summary_text = response.choices[0].message.content
        sections = summary_text.split("\n\n")
        
        return {
            "summary": sections[0],
            "key_points": sections[1].split("\n"),
            "next_actions": sections[2].split("\n")
        }
    
    async def _analyze_message(self, message: str) -> Dict:
        """Analisa uma mensagem individual para extrair características"""
        prompt = f"""
        Analise a seguinte mensagem e forneça:
        1. Nível de formalidade (0-1)
        2. Sentimento (-1 a 1)
        
        Mensagem: {message}
        """
        
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        
        # Processa a resposta para extrair os valores
        analysis = response.choices[0].message.content
        formality = float(analysis.split("\n")[0].split(":")[1])
        sentiment = float(analysis.split("\n")[1].split(":")[1])
        
        return {
            "formality": formality,
            "sentiment": sentiment
        } 