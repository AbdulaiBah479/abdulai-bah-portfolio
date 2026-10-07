#!/usr/bin/env bash
# One-time: copies Bah.Digital out of its temporary home into ~/bah-digital.
# Run in Ubuntu (WSL):  bash bootstrap.sh
set -euo pipefail
[ -d ~/bah-digital ] && { echo "~/bah-digital already exists - nothing to do."; exit 0; }
tmp=$(mktemp -d)
git clone -q --depth 1 -b claude/sweet-shannon-usgljt \
  https://github.com/AbdulaiBah479/abdulai-bah-portfolio.git "$tmp/src"
cp -r "$tmp/src/bah-digital" ~/bah-digital
rm -rf "$tmp"
cd ~/bah-digital
rm -f bootstrap.sh
git init -q -b main && git add -A && git commit -q -m "Bah.Digital foundation"
chmod +x scripts/*.sh infrastructure/postgres/init.sh
echo "Done: ~/bah-digital created. Next: cd ~/bah-digital && ./scripts/setup.sh"
