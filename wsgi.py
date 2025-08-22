"""
WSGI config for Backend project - Root level for Render deployment
"""

import os
import sys

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the WSGI application from Backend module
from Backend.wsgi import application

# This is what Gunicorn will look for
application = application
