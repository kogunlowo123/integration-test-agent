#!/bin/bash
set -euo pipefail
echo "Setting up Integration Test Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
