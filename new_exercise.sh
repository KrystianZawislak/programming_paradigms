#!/usr/bin/env bash
# Creates a new exercise folder (exN) from _template.
# Usage: ./new_exercise.sh [class|practice] [number] [title]
#   class|practice - optional, target folder: class_exercises (default) or exam_practice
#   number         - optional, defaults to the next free number in that folder
#   title          - optional, defaults to "Untitled"
set -euo pipefail

cd "$(dirname "$0")"

section="class_exercises"
author="Piotr Pawlik"
if [[ $# -ge 1 && ( "$1" == "class" || "$1" == "practice" ) ]]; then
  if [[ "$1" == "practice" ]]; then
    section="exam_practice"
    author="Claude (exam practice task)"
  fi
  shift
fi

if [[ $# -ge 1 && "$1" =~ ^[0-9]+$ ]]; then
  n="$1"; shift
else
  last=$( { find "$section" -maxdepth 1 -type d -name 'ex[0-9]*' 2>/dev/null || true; } | sed 's|.*/ex||' | sort -n | tail -1)
  n=$(( ${last:-0} + 1 ))
fi

title="${*:-Untitled}"
dir="$section/ex$n"

if [[ -e "$dir" ]]; then
  echo "error: $dir already exists" >&2
  exit 1
fi

mkdir -p "$dir"
sed -e "s/{{N}}/$n/g" -e "s/{{TITLE}}/$title/g" -e "s/{{DATE}}/$(date +%Y-%m-%d)/g" \
  -e "s/{{AUTHOR}}/$author/g" \
  _template/README.md > "$dir/README.md"

echo "created $dir/README.md"
