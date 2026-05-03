
def detect_anomalies(data):
    alerts = []

    if data["battery_level"] < 20:
        alerts.append({"alert": "Low Battery", "reason": "Battery level below 20%"})

    if data["signal_strength"] < 30:
        alerts.append({"alert": "Weak Signal", "reason": "Signal strength below threshold"})

    if data["packet_loss"] > 20:
        alerts.append({"alert": "High Packet Loss", "reason": "Packet loss above 20%"})

    if data["temperature"] > 80:
        alerts.append({"alert": "Overheating", "reason": "Temperature exceeds safe limit"})

    if data["speed"] > 100:
        alerts.append({"alert": "Unusual Speed", "reason": "Speed exceeds normal range"})

    return alerts
