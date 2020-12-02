# Usage: bash KillServer.sh python3 Server.py

lsof -ti tcp:8000 | xargs kill
$@