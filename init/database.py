import sqlite3


class UserDatabase:
    """
    Класс для работы с базой данных пользователей.
    """

    def __init__(self, db_path="users.db"):
        """
        Инициализирует соединение с базой данных.
        """
        self.connection = sqlite3.connect(db_path)  # Подключение к базе данных SQLite
        self.create_users_table()  # Создание таблицы пользователей
        self.create_results_table()  # Создание таблицы результатов

    def create_users_table(self):
        """
        Создает таблицу пользователей, если она еще не существует.
        """
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,   
                    login TEXT UNIQUE COLLATE NOCASE,  
                    email TEXT UNIQUE COLLATE NOCASE, 
                    password TEXT  
                )
            """)

    def create_results_table(self):
        """
        Создает таблицу результатов, если она еще не существует.
        """
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS results (
                    user_id INTEGER PRIMARY KEY,  
                    correct_answers INTEGER,  
                    total_questions INTEGER,  
                    correct_simulators INTEGER,  
                    total_simulators INTEGER, 
                    FOREIGN KEY(user_id) REFERENCES users(id)  
                )
            """)

    def add_user(self, login, email, password):
        """
        Добавляет нового пользователя в базу данных.
        """
        try:
            with self.connection:
                self.connection.execute("""
                    INSERT INTO users (login, email, password) VALUES (?, ?, ?)
                """, (login.lower(), email.lower(), password))
            return True  # Пользователь успешно добавлен
        except sqlite3.IntegrityError:
            return False  # Пользователь с таким логином или email уже существует

    def user_exists(self, login_or_email):
        """
        Проверяет, существует ли пользователь с заданным логином или email.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT 1 FROM users WHERE LOWER(login) = ? OR LOWER(email) = ?
        """, (login_or_email.lower(), login_or_email.lower()))
        return cursor.fetchone() is not None  # Проверка, существует ли пользователь

    def authenticate_user(self, login_or_email, password):
        """
        Аутентифицирует пользователя по логину/email и паролю.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT id FROM users WHERE (LOWER(login) = ? OR LOWER(email) = ?) AND password = ?
        """, (login_or_email.lower(), login_or_email.lower(), password))
        result = cursor.fetchone()
        return result[0] if result else None  # Возвращаем идентификатор пользователя, если аутентификация успешна

    def get_user_data(self, login_or_email):
        """
        Получает данные пользователя по логину или email.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT login, email FROM users WHERE LOWER(login) = ? OR LOWER(email) = ?
        """, (login_or_email.lower(), login_or_email.lower()))
        result = cursor.fetchone()
        if result:
            return {"login": result[0], "email": result[1]}  # Возвращаем данные пользователя
        return {"login": "Not found", "email": "Not found"}  # Пользователь не найден

    def add_test_result(self, user_id, correct_answers, total_questions):
        """
        Добавляет результат теста пользователя в базу данных.
        """
        with self.connection:
            self.connection.execute("""
                INSERT INTO results (user_id, correct_answers, total_questions) VALUES (?, ?, ?)
            """, (user_id, correct_answers, total_questions))  # Добавляем результат теста

    def update_test_result(self, user_id, correct_answers, total_questions):
        """
        Обновляет результат теста пользователя в базе данных.
        """
        with self.connection:
            self.connection.execute("""
                UPDATE results SET correct_answers = ?, total_questions = ? WHERE user_id = ?
            """, (correct_answers, total_questions, user_id))  # Обновляем результат теста

    def add_simulator_result(self, user_id, correct_simulators, total_simulators):
        """
        Добавляет результат симуляции пользователя в базу данных.
        """
        with self.connection:
            self.connection.execute("""
                INSERT INTO results (user_id, correct_simulators, total_simulators) VALUES (?, ?, ?)
            """, (user_id, correct_simulators, total_simulators))  # Добавляем результат симуляции

    def update_simulator_result(self, user_id, correct_simulators, total_simulators):
        """
        Обновляет результат симуляции пользователя в базе данных.
        """
        with self.connection:
            self.connection.execute("""
                UPDATE results SET correct_simulators = ?, total_simulators = ? WHERE user_id = ?
            """, (correct_simulators, total_simulators, user_id))  # Обновляем результат симуляции

    def get_test_results(self, user_id):
        """
        Получает результаты тестов пользователя из базы данных.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT correct_answers, total_questions FROM results WHERE user_id = ?
        """, (user_id,))
        return cursor.fetchall()  # Получаем результаты тестов пользователя

    def get_simulator_results(self, user_id):
        """
        Получает результаты симуляции пользователя из базы данных.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT correct_simulators, total_simulators FROM results WHERE user_id = ?
        """, (user_id,))
        return cursor.fetchall()  # Получаем результаты симуляций пользователя

    @staticmethod
    def validate_password(password):
        """
        Проверяет, что пароль содержит минимум 8 символов.
        """
        return len(password) >= 8  # Проверка, что пароль содержит минимум 8 символов

    def close(self):
        """
        Закрывает соединение с базой данных.
        """
        self.connection.close()  # Закрываем соединение с базой данных
