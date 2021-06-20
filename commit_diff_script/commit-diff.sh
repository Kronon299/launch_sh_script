#!/bin/bash

#echo "$(git diff HEAD^ --numstat)" | awk '/[1-9]/'
#echo "123" | awk '/[0-9][0-9][0-9]/'
git diff HEAD^ --numstat |
while IFS=" " read -r distro; do
  printf 'difference: %s\n' "$distro"
done