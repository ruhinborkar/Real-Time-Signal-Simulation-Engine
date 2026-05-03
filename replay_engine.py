
import json
from datetime import datetime

LOG_FILE = "project/outputs/logs.jsonl"

def replay(unit_id=None, alert_type=None, start_time=None, end_time=None):
    print("\nReplaying logs...\n")

    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                record = json.loads(line)

                timestamp = record["timestamp"]
                uid = record["unit_id"]
                alerts = record["alerts"]
                result = record["result"]

                # Filter: unit_id
                if unit_id and uid != unit_id:
                    continue

                # Filter: alert_type
                if alert_type:
                    if not any(alert_type in a["alert"] for a in alerts):
                        continue

                # Filter: time range
                if start_time or end_time:
                    t = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

                    if start_time and t < datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S"):
                        continue

                    if end_time and t > datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S"):
                        continue

                print({
                    "timestamp": timestamp,
                    "unit_id": uid,
                    "status": result["status"],
                    "risk_score": result["risk_score"],
                    "reasons": result["reasons"]
                })

    except FileNotFoundError:
        print("Run streaming first to generate logs.")

if __name__ == "__main__":
    replay()
