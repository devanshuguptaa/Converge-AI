"""
Agent Middleware Module

This module provides custom middleware for the AI agent.
Middleware can inject additional context into the agent's prompts,
such as relevant Slack history (RAG), user memories, or platform-specific info.

Middleware Pattern:
    Each middleware class implements a process() method that:
    1. Receives the user message and context
    2. Performs some operation (search, lookup, etc.)
    3. Returns additional context to inject into the prompt
"""

from typing import Optional

from src.utils.logger import get_logger
from src.config import config

logger = get_logger(__name__)


class RAGMiddleware:
    """
    RAG (Retrieval Augmented Generation) Middleware.
    
    This middleware searches the Slack message history for relevant context
    and injects it into the agent's prompt.
    
    It helps the agent answer questions about past conversations by providing
    relevant message history automatically.
    """
    
    def __init__(self):
        """Initialize RAG middleware."""
        self.enabled = config.rag.enabled
        logger.info("RAG middleware initialized")
    
    async def process(
        self,
        user_message: str,
        user_id: str,
        channel_id: str,
        session_id: str
    ) -> Optional[str]:
        """
        Process the user message and inject relevant context from RAG.
        
        This function:
        1. Checks if the message might benefit from RAG
        2. Searches the vector store for relevant messages
        3. Formats and returns the context
        
        Args:
            user_message: The user's message
            user_id: Slack user ID
            channel_id: Slack channel ID
            session_id: Session ID
            
        Returns:
            Optional[str]: Context to inject, or None if not applicable
        """
        if not self.enabled:
            return None
        
        try:
            # Check if message seems to be asking about past information
            # Keywords that suggest RAG might be useful
            rag_keywords = [
                "what did", "when did", "who said", "discussed", "mentioned",
                "talked about", "conversation", "yesterday", "last week",
                "remember", "recall", "find", "search"
            ]
            
            message_lower = user_message.lower()
            needs_rag = any(keyword in message_lower for keyword in rag_keywords)
            
            if not needs_rag:
                return None
            
            # Import RAG retriever - it's a StructuredTool, so call via .ainvoke()
            from src.rag.retriever import search_slack_history
            
            # Search for relevant messages - use ainvoke for StructuredTool
            results = await search_slack_history.ainvoke({
                "query": user_message,
                "channel_id": channel_id,
                "limit": config.rag.max_results
            })
            
            if not results or "No relevant messages" in results:
                return None
            
            # Format results as context
            context = "**Relevant Slack History:**\n\n"
            for i, result in enumerate(results, 1):
                context += f"{i}. {result}\n"
            
            logger.info(f"RAG middleware injected {len(results)} results")
            return context
            
        except Exception as e:
            logger.error(f"RAG middleware error: {e}", exc_info=True)
            return None


class MemoryMiddleware:
    """
    Memory Middleware.
    
    This middleware retrieves relevant memories about the user from mem0
    and injects them into the agent's prompt.
    
    It helps the agent remember user preferences, past interactions,
    and important facts across conversations.
    """
    
    def __init__(self):
        """Initialize Memory middleware."""
        self.enabled = config.memory.enabled
        logger.info("Memory middleware initialized")
    
    async def process(
        self,
        user_message: str,
        user_id: str,
        channel_id: str,
        session_id: str
    ) -> Optional[str]:
        """
        Process the user message and inject relevant memories.
        
        This function:
        1. Searches mem0 for memories about this user
        2. Formats and returns relevant memories
        
        Args:
            user_message: The user's message
            user_id: Slack user ID
            channel_id: Slack channel ID
            session_id: Session ID
            
        Returns:
            Optional[str]: Memory context to inject, or None if not applicable
        """
        if not self.enabled:
            return None
        
        try:
            # Import memory client
            from src.memory.mem0_client import search_memories
            
            # Search for relevant memories
            memories = await search_memories(
                user_id=user_id,
                query=user_message,
                limit=5
            )
            
            if not memories:
                return None
            
            # Format memories as context
            context = "**What I Remember About You:**\n\n"
            for i, memory in enumerate(memories, 1):
                context += f"{i}. {memory}\n"
            
            logger.info(f"Memory middleware injected {len(memories)} memories")
            return context
            
        except Exception as e:
            logger.error(f"Memory middleware error: {e}", exc_info=True)
            return None


class SlackContextMiddleware:
    """
    Slack Context Middleware.
    
    This middleware adds Slack-specific context to the agent's prompt,
    such as the current channel, user info, and platform capabilities.
    
    It helps the agent understand the Slack environment and use
    appropriate tools.
    """
    
    def __init__(self):
        """Initialize Slack context middleware."""
        logger.info("Slack context middleware initialized")
    
    async def process(
        self,
        user_message: str,
        user_id: str,
        channel_id: str,
        session_id: str
    ) -> Optional[str]:
        """
        Process the user message and inject Slack context.
        
        Args:
            user_message: The user's message
            user_id: Slack user ID
            channel_id: Slack channel ID
            session_id: Session ID
            
        Returns:
            Optional[str]: Slack context to inject
        """
        try:
            context = f"""**Current Context:**
- User ID: {user_id}
- Channel ID: {channel_id}
- Session ID: {session_id}

You are interacting with this user in Slack. You have access to various Slack tools
to send messages, get channel information, and more. Use them when appropriate.
"""
            return context
            
        except Exception as e:
            logger.error(f"Slack context middleware error: {e}", exc_info=True)
            return None


if __name__ == "__main__":
    # Test middleware
    import asyncio
    
    async def test():
        # Test RAG middleware
        rag = RAGMiddleware()
        context = await rag.process(
            user_message="What did we discuss about the new feature?",
            user_id="U123456",
            channel_id="C789012",
            session_id="test_session"
        )
        print(f"RAG Context: {context}")
        
        # Test Memory middleware
        memory = MemoryMiddleware()
        context = await memory.process(
            user_message="What do you remember about me?",
            user_id="U123456",
            channel_id="C789012",
            session_id="test_session"
        )
        print(f"Memory Context: {context}")
        
        # Test Slack context middleware
        slack = SlackContextMiddleware()
        context = await slack.process(
            user_message="Hello",
            user_id="U123456",
            channel_id="C789012",
            session_id="test_session"
        )
        print(f"Slack Context: {context}")
    
    asyncio.run(test())
