#!/bin/bash
# Double-click this file once to set everything up.
cd "$(dirname "$0")" || exit 1

echo "Setting up Python Playground..."

if ! command -v uv >/dev/null 2>&1 && [ ! -x "$HOME/.local/bin/uv" ]; then
    echo "Installing uv (it downloads Python for us)..."
    curl -LsSf https://astral.sh/uv/install.sh | sh || exit 1
fi
export PATH="$HOME/.local/bin:$PATH"

rm -rf .venv
uv venv --python 3.12 || exit 1
uv pip install -e . || exit 1

echo
echo "All done! Opening your first lesson..."
.venv/bin/python lessons/01_first_shapes.py
