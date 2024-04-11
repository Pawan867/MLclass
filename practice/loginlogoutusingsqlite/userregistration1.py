import hashlib
import sqlite3
import re


conn = sqlite3.connect('account.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    email TEXT NOT NULL
)
''')


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def register_user():
    username = input("Enter user ID: ")
    email = input("Enter email: ")
    if not validate_email(email):
        print("Invalid email format.")
        return
    password = input("Enter password: ")
    hashed_password = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                       (username, hashed_password, email))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("This user ID already exists.")


def login_user():
    username = input("Enter user ID: ")
    password = input("Enter password: ")
    cursor.execute(
        "SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result and hash_password(password) == result[0]:
        print("Login successful.")
    else:
        print("Invalid user ID or password.")


def update_password():
    username = input("Enter your user ID: ")
    old_password = input("Enter your old password: ")
    cursor.execute(
        "SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result and hash_password(old_password) == result[0]:
        new_password = input("Enter your new password: ")
        cursor.execute("UPDATE users SET password = ? WHERE username = ?",
                       (hash_password(new_password), username))
        conn.commit()
        print("Password updated successfully.")
    else:
        print("Invalid user ID or password.")


def delete_account():
    username = input("Enter your user ID: ")
    password = input("Enter your password: ")
    cursor.execute(
        "SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result and hash_password(password) == result[0]:
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        conn.commit()
        print("Account deleted successfully.")
    else:
        print("Invalid user ID or password.")


def main():
    while True:
        print("\nUser Management System")
        print("1. Register")
        print("2. Login")
        print("3. Update Password")
        print("4. Delete Account")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            update_password()
        elif choice == '4':
            delete_account()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
