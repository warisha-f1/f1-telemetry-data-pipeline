# F1 HD Telemetry Tools
A high-precision tool for extracting and visualizing F1 telemetry with synchronized time-delta analysis.

# Key Features
HD Output: Forced 300 DPI resolution for clear visualization.

Delta Analysis: Synchronized time-gap calculation using distance-based interpolation.

Crash-Proof: Automated data alignment to prevent ValueError and KeyError crashes.

# Tech Stack
Core: Python (3.11+)

Telemetry API: FastF1 (Official F1 timing and sensor feeds)

Data Science: Polars, NumPy, SciPy

Validation: Pydantic (Strict schema enforcement for sensor data)

Visualization: Matplotlib / Seaborn (F1-standard engineering charts)

# Trackside Goal
This project serves as a technical proof-of-concept for my goal of becoming a Trackside Data Engineer. It demonstrates the ability to manage the high-stakes, high-precision telemetry environment required by F1 teams.

# Setup & Usage
Install: 
```bash
pip install fastf1 matplotlib

# Run:
```bash
python src/telemetry_plot.py

Configure:
Change year/GP in the run_f1_analysis call at the bottom of the script.
