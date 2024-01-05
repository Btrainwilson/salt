#!/usr/bin/env bash
TEMP=$(find * -maxdepth 5 -type d | fzf) 
BASE=$(basename "$TEMP")
tmux has-session -t "$BASE" 2>/dev/null
if [ $? != 0 ]; then 
  tmux new-session -d -s "$BASE"
  tmux send-keys "cd '$TEMP'" C-m
  tmux send-keys "echo 'Creating new session $BASE'" C-m
  tmux send-keys "make start-session" C-m
  tmux send-keys 'nvim .' C-m
fi
tmux a -t "$BASE"
