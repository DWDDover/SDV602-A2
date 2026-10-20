#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON="${PYTHON:-python}"

cd "$ROOT_DIR"
exec "$PYTHON" -m unittest discover -s data_explorer/testing -p "test_*.py"
