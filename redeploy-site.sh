#!/bin/bash
set -e  # stop the script if any command fails

PROJECT_PATH="$HOME/mlh-portfolio"
SERVICE_NAME="myportfolio"

cd "$PROJECT_PATH"

echo "Pulling latest changes from origin/main.."
git fetch && git reset origin/main --hard

echo "Syncing python dependencies with uv.."
uv sync

echo "Restarting the $SERVICE_NAME service.."
sudo systemctl restart "$SERVICE_NAME"

echo "Done!"
echo "  Status:  systemctl status $SERVICE_NAME"
echo "  Logs:    journalctl -u $SERVICE_NAME -f"
