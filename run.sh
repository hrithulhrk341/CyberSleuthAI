#!/bin/bash
source venv/bin/activate
export PYTHONPATH=CyberSleuthAI
export FLASK_APP=CyberSleuthAI.app:create_app
flask run
