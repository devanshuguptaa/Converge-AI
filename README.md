<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white" alt="Slack">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

<h1 align="center">🤖 Converge AI</h1>

<p align="center">
  <strong>A Production-Ready AI Assistant for Slack with Gmail & Calendar Integration</strong>
</p>

<p align="center">
  <em>Powered by Google Gemini • MCP Architecture • RAG-Enhanced • Long-Term Memory</em>
</p>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#️-configuration)
- [Slack App Setup](#-slack-app-setup)
- [Gmail & Calendar Setup](#-gmail--calendar-setup)
- [Running the Application](#-running-the-application)
- [Usage Examples](#-usage-examples)
- [Project Structure](#-project-structure)
- [API Reference](#-api-reference)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**Converge AI** is an enterprise-grade AI assistant that lives inside your Slack workspace. It combines the power of Google Gemini's large language model with practical integrations like Gmail, Google Calendar, and intelligent memory systems to become your personal productivity companion.

Built using the **Model Context Protocol (MCP)** architecture, this assistant can:
- Read and send emails on your behalf
- Manage calendar events
- Search through your Slack message history using RAG
- Remember your preferences and past conversations
- Execute multi-step tasks autonomously

---

## ✨ Key Features

### 🧠 Intelligent Conversations
- Powered by **Google Gemini 2.0 Flash** for fast, accurate responses
- Context-aware conversations with session management
- Natural language understanding for complex requests

### 📧 Gmail Integration
| Feature | Description |
|---------|-------------|
| `list_recent_emails` | Browse your inbox with customizable filters |
| `get_email_details` | Read full email content |
| `send_email` | Compose and send emails via natural language |
| `create_draft` | Save email drafts for later |
| `summarize_email_thread` | Get AI-powered thread summaries |

### 📅 Google Calendar Integration
| Feature | Description |
|---------|-------------|
| `list_calendar_events` | View upcoming events within date ranges |
| `create_calendar_event` | Schedule new events with descriptions |

### 📚 RAG (Retrieval Augmented Generation)
- **ChromaDB** vector database for semantic search
- Automatic indexing of Slack message history
- Context injection for informed responses

### 💾 Long-Term Memory
- **mem0** integration for persistent user preferences
- Remembers past interactions across sessions
- Personalized responses based on learned context

### 🔧 MCP (Model Context Protocol)
- Clean separation between tool definitions and execution
- Permission-based access control with scopes
- Extensible architecture for additional integrations

### 💬 Slack Integration
- Real-time Socket Mode communication
- DM and channel message handling
- Reaction-based feedback system
- Thread-aware conversations

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         SLACK WORKSPACE                              │
│                              ↓ ↑                                     │
├─────────────────────────────────────────────────────────────────────┤
│                      FASTAPI APPLICATION                             │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                    Slack Bolt Handler                          │   │
│  │              (Socket Mode • Event Handlers)                    │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                              ↓                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                      MIDDLEWARE LAYER                          │   │
│  │    ┌──────────┐   ┌──────────┐   ┌─────────────────────┐     │   │
│  │    │   RAG    │   │  Memory  │   │   Slack Context     │     │   │
│  │    │Middleware│   │Middleware│   │     Middleware      │     │   │
│  │    └──────────┘   └──────────┘   └─────────────────────┘     │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                              ↓                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                  LANGCHAIN AGENT (Gemini)                      │   │
│  │                   Tool Selection • Planning                    │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                              ↓                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                       TOOL LAYER                               │   │
│  │  ┌─────────┐  ┌─────────┐  ┌──────────┐  ┌──────────────┐   │   │
│  │  │  Email  │  │Calendar │  │  Slack   │  │   RAG Tools  │   │   │
│  │  │  Tools  │  │  Tools  │  │  Tools   │  │              │   │   │
│  │  └─────────┘  └─────────┘  └──────────┘  └──────────────┘   │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                              ↓                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                    MCP INTEGRATIONS                            │   │
│  │  ┌─────────────────┐  ┌──────────────────────────────────┐   │   │
│  │  │   Gmail API     │  │      Google Calendar API         │   │   │
│  │  │  (OAuth 2.0)    │  │         (OAuth 2.0)               │   │   │
│  │  └─────────────────┘  └──────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                              ↓                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                      DATA LAYER                                │   │
│  │  ┌──────────┐   ┌──────────┐   ┌──────────────────────────┐ │   │
│  │  │ ChromaDB │   │  SQLite  │   │         mem0             │ │   │
│  │  │  (RAG)   │   │(Sessions)│   │   (Long-term Memory)     │ │   │
│  │  └──────────┘   └──────────┘   └──────────────────────────┘ │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| **LLM** | [Google Gemini 2.0 Flash](https://ai.google.dev/) |
| **Framework** | [LangChain v1](https://python.langchain.com/) |
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) |
| **Slack SDK** | [Slack Bolt for Python](https://slack.dev/bolt-python/) |
| **Vector DB** | [ChromaDB](https://www.trychroma.com/) |
| **Memory** | [mem0](https://mem0.ai/) |
| **Authentication** | Google OAuth 2.0 |
| **Containerization** | [Docker](https://www.docker.com/) |

---

## 📋 Prerequisites

- **Python 3.13+** ([Download](https://www.python.org/downloads/))
- **Slack Workspace** with admin access
- **Google Cloud Project** with Gmail & Calendar APIs enabled
- **API Keys:**
  - [Google Gemini API Key](https://aistudio.google.com/apikey)
  - [mem0 API Key](https://app.mem0.ai/) (optional)

---

## 📥 Installation

### Option 1: Standard Installation

```bash
# Clone the repository
git clone https://github.com/devanshuguptaa/Converge-AI.git
cd Converge-AI

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

### Option 2: Using UV (Faster)

```bash
# Install uv if not already installed
pip install uv

# Install dependencies with uv
uv sync
```

### Option 3: Docker

```bash
# Build and run with Docker Compose
docker-compose up --build
```

---

## ⚙️ Configuration

### 1. Create Environment File

```bash
# Copy the example configuration
cp .env.example .env
```

### 2. Configure Required Variables

Edit `.env` with your credentials:

```env
# ============================================
# SLACK CONFIGURATION (Required)
# ============================================
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
SLACK_SIGNING_SECRET=your-signing-secret

# ============================================
# GOOGLE GEMINI (Required)
# ============================================
GEMINI_API_KEY=your-gemini-api-key
GEMINI_CHAT_MODEL=gemini-flash-lite-latest
GEMINI_EMBEDDING_MODEL=models/text-embedding-004

# ============================================
# MEMORY (Optional but Recommended)
# ============================================
MEM0_API_KEY=your-mem0-api-key
MEMORY_ENABLED=true

# ============================================
# RAG SYSTEM (Optional but Recommended)
# ============================================
RAG_ENABLED=true
RAG_MAX_RESULTS=10
VECTOR_DB_PATH=./data/chromadb

# ============================================
# EMAIL & CALENDAR
# ============================================
GMAIL_CREDENTIALS_PATH=credentials/client_secret_for_gmail_and_calender.json
GMAIL_TOKEN_PATH=credentials/token_gmail.pickle
CALENDAR_TOKEN_PATH=credentials/token_calendar.pickle
```

---

## 🔧 Slack App Setup

### Step 1: Create Slack App

1. Go to [Slack API Apps](https://api.slack.com/apps)
2. Click **"Create New App"** → **"From scratch"**
3. Name your app (e.g., "Converge AI") and select your workspace

### Step 2: Configure OAuth Scopes

Navigate to **OAuth & Permissions** and add these **Bot Token Scopes**:

| Scope | Purpose |
|-------|---------|
| `app_mentions:read` | Read @mentions of your bot |
| `channels:history` | Read channel message history |
| `channels:read` | View channel information |
| `chat:write` | Send messages as the bot |
| `im:history` | Read DM history |
| `im:read` | View DM information |
| `im:write` | Send DMs |
| `users:read` | View user information |
| `reactions:write` | Add emoji reactions |

### Step 3: Enable Socket Mode

1. Navigate to **Socket Mode** in the sidebar
2. Toggle **Enable Socket Mode** ON
3. Create an **App-Level Token** with scope `connections:write`
4. Copy this token as `SLACK_APP_TOKEN`

### Step 4: Subscribe to Events

Navigate to **Event Subscriptions**:

1. Toggle **Enable Events** ON
2. Under **Subscribe to bot events**, add:
   - `app_mention`
   - `message.im`
   - `message.channels`

### Step 5: Install to Workspace

1. Go to **Install App**
2. Click **Install to Workspace**
3. Copy the **Bot User OAuth Token** as `SLACK_BOT_TOKEN`

---

## 📧 Gmail & Calendar Setup

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable the following APIs:
   - [Gmail API](https://console.cloud.google.com/apis/library/gmail.googleapis.com)
   - [Google Calendar API](https://console.cloud.google.com/apis/library/calendar-json.googleapis.com)

### Step 2: Create OAuth 2.0 Credentials

1. Navigate to **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **OAuth client ID**
3. Choose **Desktop app** as application type
4. Download the JSON file
5. Rename to `client_secret_for_gmail_and_calender.json`
6. Place in `credentials/` folder

### Step 3: Authorize the Application

```bash
# Run the authentication setup script
python setup_auth.py
```

This will:
- Open a browser for Google OAuth consent
- Create `token_gmail.pickle` and `token_calendar.pickle`
- Store them in the `credentials/` folder

---

## 🚀 Running the Application

### Development Mode

```bash
# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Run with hot reload
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode

```bash
# Run without reload
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000

# Or use the main entry point
python main.py
```

### Docker Mode

```bash
docker-compose up -d
```

### Startup Sequence

The application will:

```
✅ Validating configuration...
✅ Initializing database...
✅ Setting up RAG system (ChromaDB)...
✅ Initializing memory (mem0)...
✅ Loading MCP tools (Email, Calendar)...
✅ Starting Slack app (Socket Mode)...
🚀 Ready to receive messages!
```

---

## 💬 Usage Examples

### Basic Conversation
```
You: Hello!
Bot: Hi! I'm your AI assistant. I can help you with emails, 
     calendar management, and answer questions about your Slack history.
```

### Email Operations

**List Recent Emails:**
```
You: Show me my last 5 emails
Bot: Here are your recent emails:
     1. 📧 From: john@example.com
        Subject: Project Update
        Date: Feb 9, 2026
     ...
```

**Send Email:**
```
You: Send an email to sarah@company.com about the meeting tomorrow at 3pm
Bot: ✅ Email sent successfully!
     To: sarah@company.com
     Subject: Meeting Tomorrow
     Body: Hi Sarah, Just a reminder about our meeting tomorrow at 3pm...
```

**Summarize Thread:**
```
You: Summarize the email thread about the Q4 report
Bot: 📋 Thread Summary:
     The Q4 report discussion includes 5 emails over 3 days...
```

### Calendar Operations

**View Events:**
```
You: What's on my calendar this week?
Bot: 📅 Upcoming Events:
     • Mon Feb 10, 10:00 AM - Team Standup
     • Tue Feb 11, 2:00 PM - Client Call
     • Wed Feb 12, 9:00 AM - Project Review
```

**Create Event:**
```
You: Schedule a meeting called "Design Review" tomorrow at 2pm for 1 hour
Bot: ✅ Event created!
     📅 Design Review
     🕐 Tomorrow, 2:00 PM - 3:00 PM
```

### Memory Features
```
You: Remember that I prefer dark mode and Python
Bot: Got it! I'll remember your preferences.

[Later...]
You: What theme should I use for the new dashboard?
Bot: Based on your preferences, I'd recommend dark mode since you mentioned you prefer it!
```

### RAG Search
```
You: What did we discuss about the API redesign last week?
Bot: Based on your Slack history, the API redesign discussion included:
     • Moving to REST from GraphQL (discussed with @john)
     • Authentication changes proposed by @sarah
     • Timeline set for Q2 release
```

---

## 📁 Project Structure

```
Converge-AI/
├── 📄 main.py                    # Application entry point
├── 📄 setup_auth.py              # Google OAuth setup script
├── 📄 verify_email.py            # Email verification utility
├── 📄 requirements.txt           # Python dependencies
├── 📄 pyproject.toml             # Project metadata
├── 📄 docker-compose.yml         # Docker configuration
├── 📄 Dockerfile                 # Container definition
├── 📄 .env.example               # Environment template
│
├── 📁 src/                       # Source code
│   ├── 📄 __init__.py
│   ├── 📄 main.py                # FastAPI app & lifecycle
│   ├── 📄 config.py              # Configuration management
│   ├── 📄 database.py            # SQLite database models
│   │
│   ├── 📁 agent/                 # AI Agent
│   │   ├── 📄 core.py            # LangChain agent setup
│   │   └── 📄 middleware.py      # RAG/Memory/Context injection
│   │
│   ├── 📁 slack/                 # Slack Integration
│   │   ├── 📄 app.py             # Slack Bolt handlers
│   │   └── 📄 tools.py           # Slack action tools
│   │
│   ├── 📁 mcp/                   # Model Context Protocol
│   │   ├── 📄 registry.py        # Tool registration
│   │   ├── 📁 core/
│   │   │   ├── 📄 server.py      # MCP server
│   │   │   ├── 📄 permissions.py # Access control & scopes
│   │   │   └── 📄 context_builder.py
│   │   ├── 📁 tools/
│   │   │   ├── 📄 email_tools.py     # Gmail tools
│   │   │   └── 📄 calendar_tools.py  # Calendar tools
│   │   └── 📁 integrations/
│   │       ├── 📁 gmail/
│   │       │   ├── 📄 service.py     # Gmail API client
│   │       │   ├── 📄 reader.py      # Read operations
│   │       │   └── 📄 sender.py      # Send operations
│   │       └── 📁 calendar/
│   │           ├── 📄 service.py     # Calendar API client
│   │           ├── 📄 reader.py      # List events
│   │           └── 📄 writer.py      # Create events
│   │
│   ├── 📁 rag/                   # Retrieval Augmented Generation
│   │   ├── 📄 vectorstore.py     # ChromaDB wrapper
│   │   ├── 📄 embeddings.py      # Gemini embeddings
│   │   ├── 📄 indexer.py         # Background indexing
│   │   └── 📄 retriever.py       # Semantic search
│   │
│   ├── 📁 memory/                # Long-term Memory
│   │   └── 📄 mem0_client.py     # mem0 integration
│   │
│   ├── 📁 scheduler/             # Task Scheduling
│   │   └── 📄 tasks.py           # APScheduler tasks
│   │
│   └── 📁 utils/                 # Utilities
│       └── 📄 logger.py          # Logging configuration
│
├── 📁 credentials/               # OAuth credentials (gitignored)
│   ├── 📄 client_secret_for_gmail_and_calender.json
│   ├── 📄 token_gmail.pickle
│   └── 📄 token_calendar.pickle
│
└── 📁 data/                      # Runtime data (gitignored)
    ├── 📄 assistant.db           # SQLite database
    └── 📁 chromadb/              # Vector database
```

---

## 📡 API Reference

### MCP Scopes

| Scope | Permission |
|-------|------------|
| `GMAIL_READ` | Read emails and threads |
| `GMAIL_SEND` | Send emails and create drafts |
| `CALENDAR_READ` | View calendar events |
| `CALENDAR_WRITE` | Create and modify events |

### Email Tools

| Tool | Parameters | Returns |
|------|------------|---------|
| `list_recent_emails` | `limit: int`, `query?: str` | List of email summaries |
| `get_email_details` | `message_id: str` | Full email content |
| `get_multiple_email_details` | `message_ids: str[]` | Batch email details |
| `send_email` | `to: str`, `subject: str`, `body: str` | Send confirmation |
| `create_draft` | `to: str`, `subject: str`, `body: str` | Draft ID |
| `summarize_email_thread` | `thread_id: str` | Thread messages |

### Calendar Tools

| Tool | Parameters | Returns |
|------|------------|---------|
| `list_calendar_events` | `start_time?: str`, `end_time?: str` | List of events |
| `create_calendar_event` | `summary: str`, `start_time: str`, `end_time: str`, `description?: str` | Event confirmation |

---

## 🐛 Troubleshooting

### Configuration Errors

```
❌ Configuration errors:
   - SLACK_BOT_TOKEN is not configured
```

**Solution:** Ensure all required variables are set in `.env`:
```bash
cp .env.example .env
# Edit .env with your actual values
```

### Slack Connection Issues

```
Failed to initialize Slack app
```

**Solutions:**
1. Verify Socket Mode is enabled in Slack App settings
2. Check that `SLACK_APP_TOKEN` starts with `xapp-`
3. Ensure `SLACK_BOT_TOKEN` starts with `xoxb-`
4. Reinstall the app to your workspace

### Gmail/Calendar Authentication Errors

```
Error: invalid_grant
```

**Solution:** Re-authenticate:
```bash
# Delete existing tokens
rm credentials/token_gmail.pickle
rm credentials/token_calendar.pickle

# Re-run setup
python setup_auth.py
```

### Module Import Errors

```
ModuleNotFoundError: No module named 'fastapi'
```

**Solution:**
```bash
# Activate virtual environment first
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### ChromaDB Errors

```
Error initializing ChromaDB
```

**Solution:** Clear and rebuild:
```bash
rm -rf data/chromadb
# Restart the application
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Devanshu Gupta**

- GitHub: [@devanshuguptaa](https://github.com/devanshuguptaa)

---

<p align="center">
  <strong>Built with ❤️ using Google Gemini, LangChain, and Slack Bolt</strong>
</p>

<p align="center">
  <a href="#-table-of-contents">⬆️ Back to Top</a>
</p>
