
import csv
import time
import json

from anomaly_detector import detect_anomalies
from risk_engine import generate_output

DATA_FILE = "project/data/signals.csv"
LOG_FILE = "project/outputs/logs.jsonl"

def stream_data():
    print("Streaming started...\n")

    with open(DATA_FILE) as file:
        reader = csv.DictReader(file)

        for row in reader:
            data = {
                "timestamp": row["timestamp"],
                "unit_id": row["unit_id"],
                "signal_strength": int(row["signal_strength"]),
                "battery_level": int(row["battery_level"]),
                "speed": int(row["speed"]),
                "temperature": int(row["temperature"]),
                "packet_loss": int(row["packet_loss"]),
                "mission_status": row["mission_status"]
            }

            alerts = detect_anomalies(data)
            result = generate_output(data, alerts)

            # 🔥 Save logs (VERY IMPORTANT for replay)
            log_entry = {
                "timestamp": data["timestamp"],
                "unit_id": data["unit_id"],
                "alerts": alerts,
                "result": result
            }

            with open(LOG_FILE, "a") as f:
                f.write(json.dumps(log_entry) + "\n")

            print(result)
            time.sleep(0.2)

if __name__ == "__main__":
    stream_data()
