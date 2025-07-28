#!/bin/bash

set -e

echo "🔧 Installing TheRootLinux CLI..."

# Detect OS and architecture
OS=$(uname | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

# Define download URL
URL="https://downloads.therootlinux.com/therootlinux-cli-${OS}-${ARCH}"

# Download binary
curl -L $URL -o /usr/local/bin/therootlinux
chmod +x /usr/local/bin/therootlinux

echo "✅ therootlinux CLI installed!"