#!/bin/bash
# Compile teleparser for RHEL 9 compatibility

podman run --rm -it \
  -v $(pwd):/workspace \
  -w /workspace \
  registry.access.redhat.com/ubi9/python-311:latest \
  bash -c '
    # Install required packages
    pip install --upgrade pip
    pip install uv nuitka ordered-set zstandard

    # Install project dependencies
    uv sync --frozen

    # Compile with nuitka
    uv run python -m nuitka \
      --onefile \
      --output-dir=build \
      --output-filename=teleparser-rhel9 \
      --lto=yes \
      --jobs=8 \
      --assume-yes-for-downloads \
      ./src/teleparser/main.py

    # Fix permissions
    chmod +x build/teleparser-rhel9
  '

echo "Build complete! Binary located at: build/teleparser-rhel9"
