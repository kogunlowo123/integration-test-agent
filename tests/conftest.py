"""Test configuration for Integration Test Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "integration-test-agent", "category": "Software Engineering"}
