import os
import importlib.util
from flask import Flask
import FreedomLog

from .loaders.modules import load_modules


FreedomLog.init(
    path="logs",
    filename="application",
    max_size="10 MB",
    backups=5,
    console=False,
    format_option=2
)



def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Hello from src.app!"

    load_modules(app)  

    return app
