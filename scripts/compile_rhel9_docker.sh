#!/bin/bash
# Compile teleparser for RHEL 9 compatibility using Docker

set -e

echo "Building teleparser for RHEL 9..."

# Create a temporary output directory
mkdir -p build

docker run --rm \
  -u root \
  -v $(pwd)/src:/app/src:ro \
  -v $(pwd)/pyproject.toml:/app/pyproject.toml:ro \
  -v $(pwd)/README.md:/app/README.md:ro \
  -v $(pwd)/build:/app/build \
  registry.access.redhat.com/ubi9/python-312:latest \
  bash -c '
    set -e
    cd /app
    
    # Install system build tools
    echo "Installing system dependencies..."
    # Install EPEL for patchelf
    dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm || true
    dnf install -y gcc patchelf
    
    # Install Python build tools
    echo "Installing Python build dependencies..."
    pip install --upgrade pip
    pip install uv 
    echo 3.12 > .python-version
    uv sync
    
    # Compile with nuitka
    echo "Compiling with Nuitka..."
    uv run python -m nuitka \
      --onefile \
      --output-dir=/app/build \
      --output-filename=teleparser-rhel9 \
      --lto=yes \
      --jobs=8 \
      --assume-yes-for-downloads \
      /app/src/teleparser/main.py
    
    echo "Compilation complete!"
    ls -lh /app/build/teleparser-rhel9
  '

echo ""
echo "✅ Build complete! Binary located at: build/teleparser-rhel9"
echo "This binary is compatible with RHEL 9 and similar systems."
ls -lh build/teleparser-rhel9
