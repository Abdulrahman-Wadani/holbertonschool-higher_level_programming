#!/usr/bin/python3
from flask import jsonify, request, Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_jwt_extended import get_jwt_identity


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
auth = HTTPBasicAuth()
jwt = JWTManager(app)


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


users = {"user1": {
    "username": "user1",
    "password": generate_password_hash("password"),
    "role": "user"
}, "admin1": {
    "username": "admin1",
    "password": generate_password_hash("password"),
    "role": "admin"
}
}


@auth.verify_password
def verify_password(username, password):
    if username in users.keys():
        if check_password_hash(users[username]["password"], password):
            return users[username]
    return None


@app.route("/basic-protected")
@auth.login_required
def access():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Bad request"}), 400
    user = verify_password(data["username"], data["password"])
    if user:
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/jwt-protected")
@jwt_required()
def aaccess():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    user = get_jwt_identity()
    if user["role"] == "admin":
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    app.run()
