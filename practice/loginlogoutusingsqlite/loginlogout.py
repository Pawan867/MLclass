import hashlib
import sqlite3

# Establish a connection to an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
''')


def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def execute_command(command, params=()):
    """Executes a database command with optional parameters and commits the changes."""
    cursor.execute(command, params)
    conn.commit()


def register_user():
    """Registers a new user."""
    username = input("User ID: ")
    password = hash_password(input("Password: "))
    execute_command(
        "INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    print("User registered.")


def login_user():
    """Logs in a user."""
    username = input("User ID: ")
    password = hash_password(input("Password: "))
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    if cursor.fetchone():
        print("Login successful.")
    else:
        print("Invalid credentials.")


def update_password():
    """Updates a user's password."""
    username = input("User ID: ")
    new_password = hash_password(input("New Password: "))
    execute_command(
        "UPDATE users SET password = ? WHERE username = ?", (new_password, username))
    print("Password updated.")


def delete_account():
    """Deletes a user's account."""
    username = input("User ID: ")
    execute_command("DELETE FROM users WHERE username = ?", (username,))
    print("Account deleted.")


actions = {
    '1': register_user,
    '2': login_user,
    '3': update_password,
    '4': delete_account
}


def main():
    while True:
        print("\n1. Register\n2. Login\n3. Update Password\n4. Delete Account\n5. Exit")
        choice = input("Choose an action: ")
        if choice == '5':
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
