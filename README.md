# Real-Time-Signal-Simulation-Engine
# A deterministic, Real-Time-Signal-Simulation-Engine and risk analysis engine that simulates streaming data from multiple agents, detects anomalies using rule-based logic, assigns risk scores, and provides a replayable audit trail with a live dashboard.

## Architecture
Data Generator → Stream Simulator → Anomaly Detection → Risk Engine → Log Storage → Replay Engine → Dashboard

## Project Overview
This project simulates a dynamic environment where multiple agents continuously emit signal data. The system processes each signal in real time, evaluates risk based on predefined rules, and logs every decision for deterministic replay.

The focus is on:
* Explainability (clear rule-based alerts)
* Determinism (replay produces identical results)
* Real-time simulation (row-by-row processing)
* Observability (dashboard + logs)
* 
## Features
### 1. Simulated Dataset

* Synthetic dataset (`project/data/signals.csv`)
* Each row represents one signal event
* Fields include:

  * timestamp
  * unit_id
  * signal_strength
  * battery_level
  * speed
  * temperature
  * packet_loss
  * mission_status

## 2. Real-Time Streaming Simulation
* Processes data row-by-row
* Introduces delay to mimic live feed
* Avoids batch processing


## 3. Anomaly Detection
The system uses rule-based logic to detect abnormal conditions in incoming signals.

Examples of rules:
1. Battery level below 20% → Low Battery
2. Signal strength below threshold → Weak Signal
3. Packet loss above 20% → High Packet Loss
4. Temperature above safe limit → Overheating
5. Speed beyond normal range → Unusual Speed

Each detected anomaly generates a clear, explainable reason

## 4. Risk Scoring System
The Risk Engine is responsible for converting detected anomalies into a quantifiable risk score, classifying the overall system state, and recommending appropriate actions.

Status Classification
Based on the final risk score, the system categorizes each signal into one of four levels:

Score Range	Status	Meaning
0	         Normal	            No issues detected
1 – 30	   Warning	          Minor issues, needs monitoring
31 – 60	   High Risk	        Significant issues, requires inspection
> 60	     Critical	          Severe issues, requires immediate escalation
> Key Design Benefits
Explainability → Every score is backed by clear reasons
Deterministic Logic → Same input always produces same output
Action-Oriented → Not just detection, but decision support

## 5. Structured Output

Each processed signal generates:

```json
{
  "trace_id": "unique-id",
  "unit_id": "U7",
  "risk_score": 55,
  "status": "High Risk",
  "reasons": ["Battery level below 20%", "Speed exceeds normal range"],
  "recommended_action": "Inspect and take corrective action"
}
```

## 6. Replay Engine (Deterministic)
* Logs stored in: `project/outputs/logs.jsonl`
* Replay system allows:

  * Filtering by unit_id
  * Filtering by alert type
  * Filtering by time range
* Ensures:
  Same input → Same output (deterministic)

## 7. 📊 Streamlit Dashboard
Interactive dashboard with:
* Real-time signal table
* Risk metrics (Normal, Warning, High Risk, Critical)
* Filters (unit, status)
* Risk distribution chart
* Risk score trend visualization

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Generate dataset

```bash
python !python project/src/data_generator.py
```

### 3. Run streaming simulation

```bash
python !python project/src/stream_simulator.py
```

### 4. Replay Engine


!python project/src/replay_engine.py
'''

### 5. Launch dashboard

```bash
project/dashboard/app.py
```

---

## 📸 Dashboard Preview

<img width="1358" height="811" alt="Dashboard" src="https://github.com/user-attachments/assets/439af514-7dc5-4b4b-a3cf-7611ff119e5c" />


## Design Principles
* **Deterministic Processing** → reproducible outputs
* **Explainability** → every decision has reasons
* **Modularity** → clean separation of components
* **Scalability Ready** → can extend to ML models

## Future Improvements
* Real-time streaming via Kafka/WebSockets
* Persistent database storage
* Alert notification system

## Conclusion
This system demonstrates a complete pipeline for real-time signal monitoring, risk evaluation, and replayable decision tracking with a clean and explainable architecture.


## Author
Built as part of an AI/Data Science internship task.
Ruhin B

