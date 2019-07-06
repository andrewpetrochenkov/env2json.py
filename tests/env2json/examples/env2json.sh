#!/usr/bin/env bash
{ set +x; } 2>/dev/null

set "${BASH_SOURCE[0]%/*}"/.env
python -m env2json "$1"
