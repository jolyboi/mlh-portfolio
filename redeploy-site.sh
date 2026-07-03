#!/bin/bash 

PROJECT_PATH="$HOME/mlh-portfolio"

echo "Killing all existing sessions.."
tmux kill-server 2>/dev/null || true # ignore errors if no tmux sessions running

cd "$PROJECT_PATH"

echo "Pulling latest changes from origin/main.."
git fetch && git reset origin/main --hard

echo "Syncing python dependencies with uv.."
uv sync 

echo "Starting a new detached tmux session with a flask server.."
tmux new-session -d -s myserver "cd $PROJECT_PATH  && uv run flask run --host=0.0.0.0 --port=5000"

echo "Done!"
echo "	Attach with: tmux attach -t myserver"
