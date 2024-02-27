#!/usr/bin/python3
"""This module contains endpoint the check the status"""
from flask import jsonify
from . import app_views


@app_views.route("/status")
def return_status():
    """checks for the status"""
    return jsonify({"status": "OK"})
