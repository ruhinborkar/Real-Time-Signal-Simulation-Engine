
import uuid

ALERT_SCORES = {
    "Low Battery": 30,
    "Weak Signal": 20,
    "High Packet Loss": 25,
    "Overheating": 30,
    "Unusual Speed": 25
}

def calculate_risk(alerts):
    score = 0
    reasons = []

    for alert in alerts:
        score += ALERT_SCORES.get(alert["alert"], 0)
        reasons.append(alert["reason"])

    return score, reasons


def classify_status(score):
    if score == 0:
        return "Normal"
    elif score <= 30:
        return "Warning"
    elif score <= 60:
        return "High Risk"
    else:
        return "Critical"


def get_action(status):
    if status == "Normal":
        return "No action required"
    elif status == "Warning":
        return "Monitor and review"
    elif status == "High Risk":
        return "Inspect and take corrective action"
    else:
        return "Escalate for human review"


def generate_output(data, alerts):
    score, reasons = calculate_risk(alerts)
    status = classify_status(score)

    return {
        "trace_id": str(uuid.uuid4()),
        "unit_id": data["unit_id"],
        "risk_score": score,
        "status": status,
        "reasons": reasons,
        "recommended_action": get_action(status)
    }
