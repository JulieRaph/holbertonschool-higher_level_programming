#!/usr/bin/python3
"""API Security and Authentication Techniques"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_to_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    if (username in users and
            check_password_hash(users[username]["password"], password)):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_authentication():
    return jsonify({"Basic Auth: Access Granted"})


@app.route("/login", methods=["POST"])
def login_user():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"message: username or password required"}), 400

    if (username in users and 
            check_password_hash(users[username]["password"], password)):
        access_token = create_access_to_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"message: Invalid credentials"}), 401

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted", "user": current_user}), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    log_user = get_jwt_identity()
    user = users.get(log_user)
    if user["role"] == "admin":
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(debug=True)
