#!/bin/bash
SESSION="blog"
N=2
while tmux has-session -t "$SESSION" 2>/dev/null; do
  SESSION="blog-$N"
  N=$((N + 1))
done
tmux new-session -d -s "$SESSION" -c "$HOME/projects/nprimeau.dev" \
  "bash -c '. $HOME/.local/bin/env && claude --dangerously-skip-permissions'"

(
  # Wait for initial prompt
  while ! tmux capture-pane -t "$SESSION" -p 2>/dev/null | grep -q "❯"; do
    sleep 0.5
  done
  tmux send-keys -t "$SESSION" "/remote-control" Enter

  # Wait for /remote-control to finish then send /context
  sleep 2
  while tmux capture-pane -t "$SESSION" -p 2>/dev/null | grep -qE "Thinking|Reading|Running|Bash|⏺|✽|✻|connecting"; do
    sleep 1
  done
  sleep 1
  tmux send-keys -t "$SESSION" "/context" Enter
) &

echo "blog → tmux attach -t $SESSION"
