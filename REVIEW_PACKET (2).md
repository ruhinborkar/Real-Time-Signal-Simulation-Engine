# REVIEW PACKET

## Real-Time Signal Intelligence Monitoring System

---

## 1. Summary

This project implements a **modular, real-time signal intelligence pipeline** designed to ingest telemetry data from multiple units, detect anomalies, compute risk scores, and generate actionable insights.

The system simulates a **streaming data environment**, where records are processed incrementally and persisted for downstream analysis, replay, and visualization. The design reflects practical principles of **data engineering, monitoring systems, and pipeline architecture**.

---

## 2. Objectives

* Detect anomalous behavior in telemetry signals
* Quantify severity using a deterministic risk scoring model
* Generate actionable recommendations based on system state
* Maintain structured logs for traceability and replay
* Provide a visualization layer for monitoring and analysis

---

## 3. System Architecture

```
Data Generator → Stream Simulator → Anomaly Detector → Risk Engine → Logger → Replay Engine → Dashboard
```

The system follows a **pipeline-oriented architecture**, ensuring clear separation of responsibilities across components.

---

## 4. Data Model

Each record in the system contains:

| Field           | Description              |
| --------------- | ------------------------ |
| timestamp       | Event timestamp          |
| unit_id         | Unique device identifier |
| signal_strength | Signal quality indicator |
| battery_level   | Battery percentage       |
| speed           | Device speed             |
| temperature     | Device temperature       |
| packet_loss     | Network packet loss (%)  |
| mission_status  | Operational state        |

---

## 5. Pipeline Execution

### Entry Point (`main.py`)

* Initializes dataset generation
* Starts the streaming pipeline
* Acts as the orchestration layer

---

### Streaming Layer (`stream_simulator.py`)

* Converts numeric fields to appropriate types
* Processes records sequentially
* Introduces controlled delay (`0.2s`) to simulate real-time ingestion
* Writes structured logs to disk

---

## 6. Anomaly Detection

Anomaly detection is implemented using deterministic rules:

| Condition            | Alert            |
| -------------------- | ---------------- |
| battery_level < 20   | Low Battery      |
| signal_strength < 30 | Weak Signal      |
| packet_loss > 20     | High Packet Loss |
| temperature > 80     | Overheating      |
| speed > 100          | Unusual Speed    |

Multiple anomalies may be triggered per record.

---

## 7. Risk Evaluation

### Scoring Model

| Alert            | Score |
| ---------------- | ----- |
| Low Battery      | 30    |
| Weak Signal      | 20    |
| High Packet Loss | 25    |
| Overheating      | 30    |
| Unusual Speed    | 25    |

Total risk score is computed as the **sum of triggered alert scores**.

---

### Classification

| Score Range | Status    |
| ----------- | --------- |
| 0           | Normal    |
| 1–30        | Warning   |
| 31–60       | High Risk |
| >60         | Critical  |

---

### Action Mapping

| Status    | Recommended Action                 |
| --------- | ---------------------------------- |
| Normal    | No action required                 |
| Warning   | Monitor and review                 |
| High Risk | Inspect and take corrective action |
| Critical  | Escalate for human review          |

---

## 8. Output Contract

Each processed record generates a structured output:

```json
{
  "trace_id": "uuid",
  "unit_id": "U6",
  "risk_score": 75,
  "status": "Critical",
  "reasons": ["..."],
  "recommended_action": "Escalate for human review"
}
```

---

## 9. Logging Strategy

Logs are persisted in:

```
project/outputs/logs.jsonl
```

Each log entry contains:

* Input metadata (timestamp, unit_id)
* Detected alerts
* Risk evaluation result

### Benefits:

* Append-only structure
* Efficient replay
* Easy debugging and auditing

---

## 10. Replay Engine

The replay module enables filtered analysis of historical logs:

Supported filters:

* `unit_id`
* `alert_type`
* `time range`

### Use Cases:

* Incident investigation
* Root cause analysis
* Historical trend inspection

---

## 11. Visualization Layer

The dashboard, built using Streamlit, provides:

* Aggregated metrics (total signals, status distribution)
* Device-level filtering
* Risk distribution visualization
* Risk score trend analysis
* Tabular log inspection

---

## 12. Design Considerations

* **Modular architecture** for extensibility
* **Streaming-first design** to reflect real-world systems
* **Deterministic rules** for interpretability
* **JSONL logging** for efficient storage and replay
* **Single entry point (main.py)** for orchestration


---

## 13. Future Enhancements

* Integration with distributed streaming systems (Kafka / PubSub)
* ML-based anomaly detection models
* Real-time alerting and notification layer
* Enhanced observability (metrics, tracing)
* Live dashboard updates with streaming backend

---

## 14. Conclusion

This project demonstrates a **complete, end-to-end signal monitoring system**, covering:

* Data ingestion
* Real-time processing
* Anomaly detection
* Risk evaluation
* Logging and replay
* Visualization

It showcases a solid foundation in **data pipelines, system design, and real-time processing workflows**.

---

## 15. Author

Ms. Ruhin Sajid Borkar


