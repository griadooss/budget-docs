#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to update version file
update_version() {
    local version=$1
    local message=$2
    local date=$(date +%Y-%m-%d)

    # Read current versions.json
    local content=$(cat versions.json)

    # Add new update to updates array
    local new_update="{\"date\":\"$date\",\"version\":\"$version\",\"changes\":[\"$message\"]}"

    # Update versions.json
    jq --arg v "$version" --arg d "$date" \
       '.version = $v | .lastUpdated = $d | .updates = ['"$new_update"'] + .updates' \
       versions.json > versions.json.tmp && mv versions.json.tmp versions.json
}

# Update documentation
echo -e "${BLUE}Updating documentation...${NC}"
git pull

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo -e "${BLUE}Installing dependencies...${NC}"
    npm install
fi

# Start local server for testing
echo -e "${BLUE}Starting local server...${NC}"
SERVER_PID=$!

# Wait for server to start
sleep 5

# Prompt for update details
echo -e "${GREEN}Enter version number (e.g. 1.0.1):${NC}"
read VERSION
echo -e "${GREEN}Enter update message:${NC}"
read MESSAGE

# Update version file
update_version "$VERSION" "$MESSAGE"

# Commit changes
git add versions.json
git commit -m "docs: update to version $VERSION - $MESSAGE"
git push origin main

# Kill server
kill $SERVER_PID

echo -e "${GREEN}Documentation updated to version $VERSION${NC}"