#!/usr/bin/python3
"""This module to Develop a Simple API using Python with Flask"""

from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Return a str in root path"""
    return "Welcome to the Flask API!"


@app.route("/data")
def users():
    """Return list of users in data path"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return a str status path"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return a user data in users path"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Return a user add or not in users dict"""
    data = request.get_json()
    username = data.get("username")
    if username in users:
        return jsonify({"error": "Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
