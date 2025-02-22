#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# Get current version from versions.json
CURRENT_VERSION=$(jq -r '.version' versions.json)

# Check for updates
echo -e "${BLUE}Checking for updates...${NC}"

# Get latest version from repository
git fetch
REMOTE_VERSION=$(git show origin/main:versions.json | jq -r '.version')

if [ "$CURRENT_VERSION" != "$REMOTE_VERSION" ]; then
    echo -e "${RED}Update available!${NC}"
    echo -e "Current version: $CURRENT_VERSION"
    echo -e "Latest version: $REMOTE_VERSION"
    echo -e "\nRun ./update.sh to update"
else
    echo -e "${GREEN}You are using the latest version ($CURRENT_VERSION)${NC}"
fi