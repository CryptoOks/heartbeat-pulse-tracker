# Heartbeat Pulse Tracker

Creates timestamped snapshots every 30 minutes via GitHub Actions.
Each run writes a new JSON file: `data/YYYY-MM-DD/HHMMSS.json`.

- No external APIs (stable).
- Always a real diff (unique filename per run).
