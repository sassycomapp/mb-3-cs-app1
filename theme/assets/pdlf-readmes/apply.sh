#!/bin/bash
# Applies the README rewrite to C:\pdlf. Checks the patch first; applies nothing if the check fails. Commits nothing.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
cd /mnt/c/pdlf
git apply --check --index "$HERE/pdlf.patch" || { echo "CHECK FAILED - nothing applied"; exit 1; }
git apply --index "$HERE/pdlf.patch"
echo "Applied:"; git status --short
