"""Integration Test Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_contract_tests():
    """Test Generate consumer-driven contract tests (Pact)."""
    tools = AgentTools()
    result = await tools.generate_contract_tests(consumer="test", provider="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_api_integration_tests():
    """Test Generate API integration tests with real HTTP calls."""
    tools = AgentTools()
    result = await tools.generate_api_integration_tests(openapi_spec="test", test_framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_db_tests():
    """Test Generate database integration tests with migrations."""
    tools = AgentTools()
    result = await tools.generate_db_tests(models="test", database="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_e2e_tests():
    """Test Generate end-to-end browser tests."""
    tools = AgentTools()
    result = await tools.generate_e2e_tests(user_flows="test", framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.integration_test_agent_agent import IntegrationTestAgentAgent
    agent = IntegrationTestAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
