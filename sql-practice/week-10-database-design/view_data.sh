#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$0")"
bash build_schema.sh
sqlite3 -header -column university.db < view_data.sql
