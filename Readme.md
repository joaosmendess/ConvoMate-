# ConvoMate

ConvoMate é uma aplicação SaaS inteligente que ajuda pessoas no dia a dia a gerenciar múltiplas conversas simultâneas, como com colegas, ficantes e outras interações. Usando IA, a aplicação analisa padrões de conversa, sugere respostas automáticas, organiza conversas por prioridade e fornece resumos rápidos para evitar que o usuário perca o contexto de conversas anteriores.

## Funcionalidades

- **Análise Automática de Conversas**: Analisa o padrão de conversa de cada interlocutor, considerando tom, velocidade de resposta e tipos de mensagens (informal, formal, emojis, etc.).
- **Respostas Automáticas**: Responde automaticamente de forma apropriada com base no padrão identificado de cada conversa.
- **Organização por Prioridade**: Organiza conversas por prioridade, destacando aquelas que precisam de resposta urgente.
- **Resumos Rápidos**: Fornece resumos rápidos das conversas para facilitar a consulta e evitar perda de contexto.
- **Integração com Mensageiros**: Integra com plataformas de mensagens como WhatsApp.

## Como Funciona

1. **Análise de Padrão de Conversa**: O sistema analisa automaticamente as conversas em tempo real, identificando o estilo e tom de cada interlocutor.
2. **Resposta Automática**: Com base na análise do padrão de conversa, o sistema sugere e envia respostas automáticas, mantendo o fluxo natural das interações.
3. **Gerenciamento de Prioridades**: O ConvoMate organiza as conversas por urgência, destacando aquelas que precisam de atenção imediata.
4. **Resumos e Revisões**: O ConvoMate gera resumos de conversas para que os usuários não percam o contexto, facilitando a revisão posterior.

## Estrutura do Projeto

```
convomate/
├── app/
│   ├── main.py           # Aplicação FastAPI principal
│   ├── models.py         # Modelos de dados
│   ├── routes.py         # Rotas da API
│   └── ai_services.py    # Serviços de IA
├── requirements.txt      # Dependências do projeto
└── .env.example         # Exemplo de variáveis de ambiente
```

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/convomate.git
cd convomate
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Execute a aplicação:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

- `POST /conversations/analyze`: Analisa o padrão de uma conversa
- `POST /conversations/generate-response`: Gera uma resposta apropriada
- `POST /conversations/summarize`: Gera um resumo da conversa
- `GET /conversations/{conversation_id}/priority`: Calcula a prioridade de uma conversa
- `GET /conversations/{conversation_id}/pattern`: Retorna o padrão de conversa identificado

## Privacidade e Segurança

- Todas as mensagens são criptografadas em trânsito e em repouso
- Os dados são armazenados em servidores seguros
- Os usuários têm controle total sobre suas conversas e dados
- A integração com mensageiros segue as políticas de privacidade de cada plataforma

## Monetização

O ConvoMate oferece diferentes planos:

- **Plano Gratuito**: Funcionalidades básicas com limite de conversas
- **Plano Pro**: Recursos avançados, mais conversas e priorização
- **Plano Empresarial**: Recursos personalizados para equipes

## Contribuindo

Contribuições são bem-vindas! Por favor, leia nosso guia de contribuição antes de enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.