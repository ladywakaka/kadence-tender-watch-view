#!/bin/sh
# Usage: scripts/encrypt.sh <snapshot.html>  -> writes src/snapshot.html.enc (key from macOS Keychain)
set -e
KEY=$(security find-generic-password -s kadence-tender-view-source-key -w)
SOURCE_KEY="$KEY" openssl enc -aes-256-cbc -pbkdf2 -iter 200000 -md sha256 -salt \
  -in "$1" -out "$(dirname "$0")/../src/snapshot.html.enc" -pass env:SOURCE_KEY
