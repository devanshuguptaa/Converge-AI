# Slack AI Assistant 🤖

A production-ready AI assistant for Slack powered by Google Gemini, featuring RAG (Retrieval Augmented Generation), long-term memory, and GitHub/Notion integration.

## ✨ Features

- **🧠 Smart Conversations**: Powered by Google Gemini 2.0 Flash
- **📚 RAG System**: Semantic search across Slack message history using ChromaDB
- **💾 Long-Term Memory**: Remembers user preferences and context with mem0
- **🔧 Tool Integration**: GitHub and Notion integration via MCP (Model Context Protocol)
- **⏰ Task Scheduling**: Set reminders and schedule messages
- **🎯 Context-Aware**: Maintains conversation history and session management

## 🏗️ Architecture

```
FastAPI Application
    ↓
Slack Webhook → Slack Bolt Handler
    ↓
LangChain v1 Agent (Gemini)
    ↓
┌─────────┬──────────┬─────────┬──────────┐
│   RAG   │  Memory  │   MCP   │  Slack   │
│ChromaDB │  mem0    │ GitHub  │  Tools   │
│         │          │ Notion  │          │
└─────────┴──────────┴─────────┴──────────┘
```

## 📋 Prerequisites

- Python 3.13+
- Slack workspace with admin access
- Google Gemini API key
- mem0 API key (optional, for memory features)
- GitHub Personal Access Token (optional, for GitHub integration)
- Notion Integration Token (optional, for Notion integration)

## 🚀 Quick Start

### 1. Clone and Setup

```bash
cd AI-assitant

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy the example environment file
copy .env.example .env

# Edit .env and fill in your API keys
notepad .env
```

**Required Configuration:**
- `SLACK_BOT_TOKEN` - Get from https://api.slack.com/apps
- `SLACK_APP_TOKEN` - Get from https://api.slack.com/apps
- `SLACK_SIGNING_SECRET` - Get from https://api.slack.com/apps
- `GEMINI_API_KEY` - Get from https://aistudio.google.com/apikey

**Optional Configuration:**
- `MEM0_API_KEY` - For long-term memory (https://app.mem0.ai/)
- `GITHUB_PERSONAL_ACCESS_TOKEN` - For GitHub integration
- `NOTION_API_TOKEN` - For Notion integration

### 3. Set Up Slack App

1. Go to https://api.slack.com/apps
2. Click "Create New App" → "From scratch"
3. Name your app and select your workspace
4. Configure the following:

**OAuth & Permissions:**
- Add these Bot Token Scopes:
  - `app_mentions:read`
  - `channels:history`
  - `channels:read`
  - `chat:write`
  - `im:history`
  - `im:read`
  - `im:write`
  - `users:read`
  - `reactions:write`

**Socket Mode:**
- Enable Socket Mode
- Create an App-Level Token with `connections:write` scope

**Event Subscriptions:**
- Enable Events
- Subscribe to these bot events:
  - `app_mention`
  - `message.im`
  - `message.channels`

### 4. Run the Application

```bash
# Activate virtual environment
.venv\Scripts\activate

# Run with uvicorn
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

The application will:
1. ✅ Validate configuration
2. ✅ Initialize database
3. ✅ Set up RAG system (if enabled)
4. ✅ Initialize memory (if enabled)
5. ✅ Connect to MCP servers (if enabled)
6. ✅ Start Slack app
7. 🚀 Ready to receive messages!

## 📖 Usage Examples

### Basic Conversation
```
You: Hello!
Bot: Hi! How can I help you today?
```

### RAG Search
```
You: What did we discuss about the new feature yesterday?
Bot: [Searches Slack history and provides context-aware answer]
```

### Memory
```
You: Remember that I prefer Python over JavaScript
Bot: Got it! I'll remember that you prefer Python over JavaScript.

[Later...]
You: What programming language should I use?
Bot: Based on what I know about you, I'd recommend Python since you prefer it over JavaScript.
```

### GitHub Integration
```
You: Create a GitHub issue titled "Fix login bug" in the main repo
Bot: [Creates issue and provides link]
```

### Task Scheduling
```
You: Remind me tomorrow at 10am to review the PR
Bot: [Sets reminder and confirms]
```

## 🛠️ Project Structure

```
AI-assitant/
├── src/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration management
│   ├── database.py          # SQLite database models
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── logger.py        # Logging utility
│   │
│   ├── slack/               # Slack integration (TODO)
│   │   ├── __init__.py
│   │   ├── app.py          # Slack Bolt app
│   │   ├── handlers.py     # Event handlers
│   │   └── tools.py        # Slack action tools
│   │
│   ├── agent/               # AI Agent (TODO)
│   │   ├── __init__.py
│   │   ├── core.py         # LangChain agent
│   │   └── middleware.py   # Custom middleware
│   │
│   ├── rag/                 # RAG system (TODO)
│   │   ├── __init__.py
│   │   ├── vectorstore.py  # ChromaDB
│   │   ├── embeddings.py   # Gemini embeddings
│   │   ├── indexer.py      # Background indexer
│   │   └── retriever.py    # Semantic search
│   │
│   ├── memory/              # Memory system (TODO)
│   │   ├── __init__.py
│   │   └── mem0_client.py  # mem0 integration
│   │
│   ├── mcp/                 # MCP integration (TODO)
│   │   ├── __init__.py
│   │   ├── client.py       # MCP client
│   │   ├── config.py       # MCP configuration
│   │   └── tools.py        # Tool converter
│   │
│   └── scheduler/           # Task scheduler (TODO)
│       ├── __init__.py
│       └── tasks.py        # APScheduler
│
├── data/                    # Data directory (created at runtime)
│   ├── chromadb/           # Vector database
│   └── assistant.db        # SQLite database
│
├── .env.example            # Environment template
├── .env                    # Your configuration (gitignored)
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project metadata
└── README.md              # This file
```

## 🔧 Configuration Options

See `.env.example` for all available configuration options.

**Key Settings:**
- `GEMINI_CHAT_MODEL` - Gemini model for chat (default: gemini-2.0-flash-exp)
- `GEMINI_EMBEDDING_MODEL` - Model for embeddings (default: text-embedding-004)
- `RAG_ENABLED` - Enable/disable RAG (default: true)
- `MEMORY_ENABLED` - Enable/disable memory (default: true)
- `MCP_ENABLED` - Enable/disable MCP (default: true)
- `LOG_LEVEL` - Logging level (DEBUG, INFO, WARNING, ERROR)

## 🐛 Troubleshooting

### Configuration Errors
```
❌ Configuration errors:
  - SLACK_BOT_TOKEN is not configured
```
**Solution**: Make sure you've copied `.env.example` to `.env` and filled in all required values.

### Import Errors
```
ModuleNotFoundError: No module named 'fastapi'
```
**Solution**: Make sure you've activated the virtual environment and installed dependencies:
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

### Slack Connection Issues
```
Failed to initialize Slack app
```
**Solution**: 
1. Check that Socket Mode is enabled in your Slack app
2. Verify your `SLACK_APP_TOKEN` starts with `xapp-`
3. Ensure your `SLACK_BOT_TOKEN` starts with `xoxb-`

## 📚 Development Status

**✅ Completed:**
- [x] Project setup and dependencies
- [x] Configuration management
- [x] Logging system
- [x] Database schema
- [x] FastAPI application structure

**🚧 In Progress:**
- [ ] Slack integration
- [ ] AI Agent with LangChain v1
- [ ] RAG system
- [ ] Memory system
- [ ] MCP integration
- [ ] Task scheduler

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

This is a personal project, but suggestions and feedback are welcome!

## 📧 Support

For issues or questions, please check the troubleshooting section above or review the comprehensive docstrings in the source code.

---

**Built with ❤️ using:**
- FastAPI
- Google Gemini
- LangChain v1
- ChromaDB
- mem0
- Slack Bolt
