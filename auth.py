import os
import json

# Path to users data file
USERS_JSON = "data/users.json"

def load_users():
    if not os.path.exists(USERS_JSON):
        return []
    try:
        with open(USERS_JSON, "r") as f:
            content = f.read().strip()
            return json.loads(content) if content else []
    except json.JSONDecodeError:
        return []

def save_user(user_data):
    users = load_users()
    users.append(user_data)
    os.makedirs("data", exist_ok=True)
    with open(USERS_JSON, "w") as f:
        json.dump(users, f, indent=4)

def username_exists(username):
    users = load_users()
    return any(user["username"] == username for user in users)

def validate_credentials(username, password):
    users = load_users()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None
