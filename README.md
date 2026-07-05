# Integration Test Agent

[![CI](https://github.com/kogunlowo123/integration-test-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/integration-test-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Software Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Integration and E2E test automation agent that generates contract tests, API integration tests, database integration tests, and end-to-end workflow tests with automatic test environment provisioning and teardown.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_contract_tests` | Generate consumer-driven contract tests (Pact) |
| `generate_api_integration_tests` | Generate API integration tests with real HTTP calls |
| `generate_db_tests` | Generate database integration tests with migrations |
| `generate_e2e_tests` | Generate end-to-end browser tests |
| `provision_test_environment` | Spin up test dependencies using Testcontainers |
| `generate_test_fixtures` | Generate realistic test data and fixtures |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/integration/contract` | Generate contract tests |
| `POST` | `/api/v1/integration/api` | Generate API integration tests |
| `POST` | `/api/v1/integration/database` | Generate database tests |
| `POST` | `/api/v1/integration/e2e` | Generate E2E tests |
| `POST` | `/api/v1/integration/environment` | Provision test environment |
| `POST` | `/api/v1/integration/fixtures` | Generate test fixtures |

## Features

- Contract Testing
- Api Integration Tests
- Db Integration Tests
- E2E Tests
- Test Env Provisioning

## Integrations

- Testcontainers
- Playwright Runner
- Pact Broker
- Test Reporter

## Architecture

```
integration-test-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── integration_test_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LLM + Testcontainers + Playwright**

---

Built as part of the Enterprise AI Agent Platform.
