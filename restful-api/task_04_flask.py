#!/usr/bin/python3
""" 433 34  """


from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    return "OK"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    user_info = users.get(username)
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        new_user = request.get_json()

        if not new_user:
            return jsonify({"error": "Invalid JSON"}), 400

    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    new_user["username"] = username
    users[username] = new_user

    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201

if __name__ == "__main__":
    app.run()
