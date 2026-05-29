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
  # Wait until the agent is fully ready (status bar appears)
  while ! tmux capture-pane -t "$SESSION" -p 2>/dev/null | grep -q "bypass permissions"; do
    sleep 0.5
  done
  tmux send-keys -t "$SESSION" "/remote-control" Enter

) &

echo "blog → tmux attach -t $SESSION"
