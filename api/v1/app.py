#!/usr/bin/python3
"""This module contains the flask web app"""
import os
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def close_storage(exception):
    """close the connection to the storage engine after each req"""
    storage.close()


if __name__ == "__main__":
    app.run(threaded=True,
            host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', 5000)))
