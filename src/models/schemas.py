"""Integration Test Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class ContractTestRequest(BaseModel):
    """ContractTestRequest for Integration Test Agent."""
    consumer: str
    provider: str
    interactions: list[dict]


class E2ETestRequest(BaseModel):
    """E2ETestRequest for Integration Test Agent."""
    user_flows: list[dict]
    framework: str = 'playwright'
    browsers: list[str] = ['chromium']


class TestEnvironmentSpec(BaseModel):
    """TestEnvironmentSpec for Integration Test Agent."""
    services: list[str]
    database: str | None
    cache: str | None
    queue: str | None

