from flask import Blueprint, render_template, jsonify
from datetime import datetime
import os
import json

dashboard_bp = Blueprint('dashboard', __name__)

ALERTS_FILE = os.path.join(os.path.dirname(__file__), 'alerts/alerts.txt')

def load_alerts():
    alerts = []
    try:
        with open(ALERTS_FILE, 'r') as f:
            for line in f:
                alerts.append(json.loads(line.strip()))
    except Exception as e:
        print(f"[!] Failed to load alerts: {e}")
    return alerts

@dashboard_bp.route("/")
def dashboard():
    alerts = load_alerts()
    return render_template("dashboard.html", alerts=alerts, current_year=datetime.now().year)

# ✅ Add this route for the incident replay API
@dashboard_bp.route("/api/replay-alerts")
def replay_alerts():
    alerts = load_alerts()
    return jsonify(alerts)
