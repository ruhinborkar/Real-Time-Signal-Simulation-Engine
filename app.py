import streamlit as st
import pandas as pd
import json
import os

LOG_FILE = "project/outputs/logs.jsonl"

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Signal Intelligence Dashboard",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("📡 Real-Time Signal Intelligence Monitoring Dashboard")
st.caption("Real-time signal analysis with risk scoring and replay insights")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_logs():
    if not os.path.exists(LOG_FILE):
        return pd.DataFrame()

    data = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            r = json.loads(line)
            data.append({
                "timestamp": r["timestamp"],
                "unit_id": r["unit_id"],
                "status": r["result"]["status"],
                "risk_score": r["result"]["risk_score"],
                "reasons": ", ".join(r["result"]["reasons"])
            })
    return pd.DataFrame(data)

df = load_logs()

# -----------------------------
# NO DATA HANDLING
# -----------------------------
if df.empty:
    st.warning("⚠ No logs found. Run streaming first.")
    st.stop()

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filters")

unit_filter = st.sidebar.selectbox(
    "Select Unit",
    ["All"] + sorted(df["unit_id"].unique().tolist())
)

status_filter = st.sidebar.selectbox(
    "Select Status",
    ["All", "Normal", "Warning", "High Risk", "Critical"]
)

# Apply filters
if unit_filter != "All":
    df = df[df["unit_id"] == unit_filter]

if status_filter != "All":
    df = df[df["status"] == status_filter]

# -----------------------------
# METRICS
# -----------------------------
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Signals", len(df))
col2.metric("Normal", (df["status"] == "Normal").sum())
col3.metric("Warning", (df["status"] == "Warning").sum())
col4.metric("High Risk", (df["status"] == "High Risk").sum())
col5.metric("Critical", (df["status"] == "Critical").sum())

st.divider()

# -----------------------------
# TABLE
# -----------------------------
st.subheader("📋 Signal Logs")
st.dataframe(df, use_container_width=True)

# -----------------------------
# CHARTS
# -----------------------------
colA, colB = st.columns(2)

with colA:
    st.subheader("📊 Risk Distribution")
    st.bar_chart(df["status"].value_counts())

with colB:
    st.subheader("📈 Risk Score Trend")
    st.line_chart(df["risk_score"])
