#!/usr/bin/python3
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}
    

@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def addUser():
    new_user = request.get_json(silent=True)
    if not new_user:
        return jsonify({"error": "Invalid JSON"}), 400
    if "username" not in new_user or not new_user["username"]:
        return jsonify({"error": "Username is required"}), 400
    if new_user["username"] in users:
        return jsonify({"error": "Username already exists"}), 409
    users[new_user["username"]] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
