#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$0")"

if sqlite3 university.db ".tables" | grep -q "students"; then
  echo "Schema already exists; no changes were made."
else
  sqlite3 university.db < schema.sql
fi

sqlite3 university.db < seed_data.sql
sqlite3 university.db ".tables"
