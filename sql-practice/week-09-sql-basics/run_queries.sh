#!/usr/bin/env bash

cd "$(dirname "$0")"
sqlite3 -header -column learning.db < queries.sql
