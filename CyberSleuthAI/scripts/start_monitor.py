from app.core.log_monitor import watch_auth_log
from app.core.behavior_ai import analyze_behavior

if __name__ == "__main__":
    print("🔍 CyberSleuth AI Log Monitoring Started...")
    watch_auth_log(analyze_behavior)
