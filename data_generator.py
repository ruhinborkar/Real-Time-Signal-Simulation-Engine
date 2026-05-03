
import csv
import random
from datetime import datetime, timedelta
import os

OUTPUT_FILE = "project/data/signals.csv"

def generate_dataset(rows=1000):
    os.makedirs("project/data", exist_ok=True)

    start_time = datetime.now()

    with open(OUTPUT_FILE, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "timestamp", "unit_id", "signal_strength",
            "battery_level", "speed", "temperature",
            "packet_loss", "mission_status"
        ])

        for i in range(rows):
            timestamp = start_time + timedelta(seconds=i)

            writer.writerow([
                timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                f"U{random.randint(1,10)}",
                random.randint(10, 100),
                random.randint(5, 100),
                random.randint(0, 150),
                random.randint(20, 100),
                random.randint(0, 30),
                random.choice(["ACTIVE", "IDLE", "RETURNING", "ERROR"])
            ])

    print("Dataset created ✅")

if __name__ == "__main__":
    generate_dataset()
