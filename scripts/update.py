# scripts/update.py
import json
import pathlib
import hashlib
from datetime import datetime, timezone
import os
import random

def make_payload():
    # UTC timestamp
    dt = datetime.now(timezone.utc)
    iso = dt.isoformat(timespec="seconds")
    # small changing salt to guarantee diff even if times collide
    salt = os.urandom(8).hex()
    # pseudo metrics so it looks "alive"
    metrics = {
        "uptimePulse": random.randint(50, 100),   # 50-100
        "loadAvgLite": round(random.uniform(0.1, 1.5), 2),
    }
    # content hash for fun
    h = hashlib.sha256(f"{iso}-{salt}-{metrics}".encode()).hexdigest()
    return dt, {
        "ts": iso,
        "source": "heartbeat-pulse-tracker",
        "metrics": metrics,
        "hash": h
    }

def write_snapshot(dt, payload):
    folder = pathlib.Path("data") / dt.strftime("%Y-%m-%d")
    folder.mkdir(parents=True, exist_ok=True)
    outpath = folder / f"{dt.strftime('%H%M%S')}.json"
    outpath.write_text(json.dumps(payload, indent=2))
    print(f"[update.py] wrote file: {outpath}")

if __name__ == "__main__":
    dt, payload = make_payload()
    write_snapshot(dt, payload)
