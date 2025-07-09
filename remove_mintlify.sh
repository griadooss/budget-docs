#!/bin/bash

# Remove Mintlify config and cache
rm -f mint.json
rm -rf .mintlify .mintlify-cache

# Remove Mintlify starter and OP docs if not needed
rm -rf docs_OP

# Remove Mintlify from .gitignore
sed -i '/\.mintlify\//d' .gitignore
sed -i '/\.mintlify-cache\//d' .gitignore

# Remove Mintlify from package.json and package-lock.json
sed -i '/mintlify/d' package.json
sed -i '/mintlify/d' package-lock.json
sed -i '/@mintlify\/cli/d' package.json
sed -i '/@mintlify\/cli/d' package-lock.json

# Remove Mintlify scripts from package.json
sed -i '/"dev": "mintlify dev",/d' package.json
sed -i '/"start": "mintlify dev",/d' package.json

# Remove Mintlify from update.sh
sed -i '/mintlify/d' update.sh

# Remove Mintlify GitHub Actions workflows
rm -f .github/workflows/mintlify*.yml

# Remove Mintlify images/assets from docs (optional, manual review recommended)
# grep -rl 'mintlify-assets' docs/ | xargs rm -f

# Remove Mintlify references from all Markdown files
grep -ril 'mintlify' docs/ | xargs sed -i '/mintlify/d'

# Uninstall Mintlify from node_modules (if using npm)
npm uninstall @mintlify/cli mintlify

echo "Mintlify cleanup complete!"
