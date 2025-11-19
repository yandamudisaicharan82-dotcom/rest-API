from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage (dictionary)
users = {}

# Home route
@app.route("/")
def home():
    return "User Management API is running!"


# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


# GET user by ID
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"}), 404


# POST - Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user_id = data.get("id")

    if user_id in users:
        return jsonify({"error": "User already exists"}), 400

    users[user_id] = {
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify({"message": "User added successfully"}), 201


# PUT - Update a user
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    users[user_id].update(data)
    return jsonify({"message": "User updated successfully"})


# DELETE - Remove a user
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
