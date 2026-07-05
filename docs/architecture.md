# Integration Test Agent Architecture

Integration and E2E test automation agent that generates contract tests, API integration tests, database integration tests, and end-to-end workflow tests with automatic test environment provisioning and teardown.

## Domain Tools

- **generate_contract_tests**: Generate consumer-driven contract tests (Pact)
- **generate_api_integration_tests**: Generate API integration tests with real HTTP calls
- **generate_db_tests**: Generate database integration tests with migrations
- **generate_e2e_tests**: Generate end-to-end browser tests
- **provision_test_environment**: Spin up test dependencies using Testcontainers
- **generate_test_fixtures**: Generate realistic test data and fixtures