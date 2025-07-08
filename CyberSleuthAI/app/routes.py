from flask import Blueprint, render_template, jsonify
from datetime import datetime
import json
import os

dashboard_bp = Blueprint("dashboard", __name__)

ALERTS_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../alerts/alerts.txt"))

@dashboard_bp.route("/")
def dashboard():
    return render_template("dashboard.html", current_year=datetime.now().year)

@dashboard_bp.route("/api/alerts")
def get_alerts():
    alerts = []
    if os.path.exists(ALERTS_FILE):
        with open(ALERTS_FILE, "r") as f:
            for line in f:
                try:
                    alerts.append(json.loads(line))
                except:
                    continue
    return jsonify(alerts)

@dashboard_bp.route("/api/replay-alerts")
def get_replay_alerts():
    # You can customize this logic to limit replay to last N hours or entries
    return get_alerts()
