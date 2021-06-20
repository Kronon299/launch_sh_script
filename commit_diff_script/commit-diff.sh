#!/bin/bash

git diff HEAD~3..HEAD --numstat |
while read -r line; do
  name=$(echo $line | awk '{print $3}')
  added=$(echo $line | awk '{print $1}')
  removed=$(echo $line | awk '{print $2}')
  printf '%s: %s lines added, %s lines removed.\n' "$name" "$added" "$removed"
done