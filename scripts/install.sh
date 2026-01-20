#!/bin/bash
set -e

# shadcn-svelte Skill Installer
# This script installs the shadcn-svelte skill for Claude Code

SKILL_NAME="shadcn-svelte"
INSTALL_DIR="$HOME/.claude/skills/$SKILL_NAME"
REPO="antstanley/shadcn-svelte-skill"

# Version is baked in at release time
VERSION="__VERSION__"

echo "Installing $SKILL_NAME skill v$VERSION..."

# Create skill directory
mkdir -p "$INSTALL_DIR"

# Download the skill file
SKILL_URL="https://github.com/$REPO/releases/download/v$VERSION/$SKILL_NAME.skill"
SKILL_FILE="$INSTALL_DIR/$SKILL_NAME.skill"

echo "Downloading from $SKILL_URL..."
curl -fsSL "$SKILL_URL" -o "$SKILL_FILE"

# Extract the skill (it's a zip file)
echo "Extracting skill..."
unzip -o -q "$SKILL_FILE" -d "$INSTALL_DIR"

# Remove the .skill archive
rm "$SKILL_FILE"

echo ""
echo "Successfully installed $SKILL_NAME skill to $INSTALL_DIR"
echo ""
echo "The skill will be available in Claude Code for projects in this directory."
echo "You can also copy the skill folder to any project's .claude/skills/ directory."
