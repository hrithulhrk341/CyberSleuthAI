from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register routes
    from CyberSleuthAI.app.routes import dashboard_bp
    app.register_blueprint(dashboard_bp)

    return app
