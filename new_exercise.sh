#!/usr/bin/env bash
# Creates a new exercise folder from _template.
# Usage: ./new_exercise.sh [practice] <topic> <name> [title]
#   practice - optional, create it in exam_practice/ instead of class_exercises/
#   topic    - topic folder or its number, e.g. 6 or 6_objects_members_and_inheritance
#   name     - folder name (snake_case), e.g. fraction_class
#   title    - optional, README title, defaults to "Untitled"
# The exercise number is the next free one in the section (numbers are global, not per topic).
set -euo pipefail

cd "$(dirname "$0")"

section="class_exercises"
author="Piotr Pawlik"
if [[ $# -ge 1 && "$1" == "practice" ]]; then
  section="exam_practice"
  author="Claude (exam practice task)"
  shift
fi

if [[ $# -lt 2 ]]; then
  echo "usage: $0 [practice] <topic> <name> [title]" >&2
  echo "topics:" >&2
  ls -1 "$section" >&2
  exit 1
fi

topic="$1"; name="$2"; shift 2
if [[ "$topic" =~ ^[0-9]+$ ]]; then
  match=$(find "$section" -mindepth 1 -maxdepth 1 -type d -name "${topic}_*" | head -1)
  if [[ -z "$match" ]]; then
    echo "error: no topic $topic in $section/ (create the folder ${topic}_<topic_name> first)" >&2
    exit 1
  fi
  topic=$(basename "$match")
fi

last=$( { find "$section" -mindepth 2 -maxdepth 2 -type d -name '[0-9]*_*' 2>/dev/null || true; } \
  | sed 's|.*/||; s|_.*||' | sort -n | tail -1)
n=$(( 10#${last:-0} + 1 ))
title="${*:-Untitled}"
dir="$section/$topic/$(printf '%02d' "$n")_$name"

if [[ -e "$dir" ]]; then
  echo "error: $dir already exists" >&2
  exit 1
fi

mkdir -p "$dir"
sed -e "s/{{N}}/$n/g" -e "s/{{TITLE}}/$title/g" -e "s/{{DATE}}/$(date +%Y-%m-%d)/g" \
  -e "s/{{AUTHOR}}/$author/g" \
  _template/README.md > "$dir/README.md"

echo "created $dir/README.md"
