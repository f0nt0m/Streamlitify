import sqlite3

class UserDatabase:
    def __init__(self, db_path="users.db"):
        self.connection = sqlite3.connect(db_path)
        self.create_users_table()

    def create_users_table(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    login TEXT UNIQUE,
                    email TEXT UNIQUE,
                    password TEXT
                )
            """)

    def add_user(self, login, email, password):
        try:
            with self.connection:
                self.connection.execute("""
                    INSERT INTO users (login, email, password) VALUES (?, ?, ?)
                """, (login, email, password))
            return True
        except sqlite3.IntegrityError:
            return False

    def user_exists(self, login_or_email):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT 1 FROM users WHERE login = ? OR email = ?
        """, (login_or_email, login_or_email))
        return cursor.fetchone() is not None

    def authenticate_user(self, login_or_email, password):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT 1 FROM users WHERE (login = ? OR email = ?) AND password = ?
        """, (login_or_email, login_or_email, password))
        return cursor.fetchone() is not None

    def get_user_data(self, login_or_email):
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT login, email FROM users WHERE login = ? OR email = ?
        """, (login_or_email, login_or_email))
        result = cursor.fetchone()
        if result:
            return {"login": result[0], "email": result[1]}
        return {"login": "Not found", "email": "Not found"}

    @staticmethod
    def validate_password(password):
        return len(password) >= 8

    def close(self):
        self.connection.close()
