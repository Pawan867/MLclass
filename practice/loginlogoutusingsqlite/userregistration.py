import sqlite3
import bcrypt
import re


conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    logged_in INTEGER DEFAULT 0
)
''')


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def register_user(username, email, password):
    if not validate_email(email):
        print("Invalid email format.")
        return

    hashed_password = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                       (username, hashed_password, email))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")


def login_user(username, password):
    cursor.execute(
        "SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        cursor.execute(
            "UPDATE users SET logged_in = 1 WHERE username = ?", (username,))
        conn.commit()
        print("Login successful.")
    else:
        print("Invalid credentials.")


users_data = [
    ("pawan_123", "ipawanacharya@gmail.com", "pawan123"),
    ("sarita_123", "pawan.acharya867@gmail.com.com", "acharya123"),
]
for username, email, password in users_data:
    register_user(username, email, password)
