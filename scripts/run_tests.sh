#!/bin/bash
cd "$(dirname "$0")/.." || exit 1
uv run python -m unittest discover -v tests/
