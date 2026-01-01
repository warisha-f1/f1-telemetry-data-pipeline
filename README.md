# F1 HD Telemetry Tools
A high-precision tool for extracting and visualizing F1 telemetry with synchronized time-delta analysis.

# Key Features
HD Output: Forced 300 DPI resolution for clear visualization.

Delta Analysis: Synchronized time-gap calculation using distance-based interpolation.

Crash-Proof: Automated data alignment to prevent ValueError and KeyError crashes.

# Setup & Usage
Install: 
```bash
pip install fastf1 matplotlib

# Run:
```bash
python telemetry_plot.py

Configure:
Change year/GP in the run_f1_analysis call at the bottom of the script.
