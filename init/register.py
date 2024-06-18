import flet as ft
import re
from init.basescreen import BaseScreen
from init.database import UserDatabase


class RegisterScreen(BaseScreen):
    """
    Экран регистрации нового пользователя.
    """

    def __init__(self, page, app):
        """
        Инициализирует экран регистрации.
        """
        super().__init__(page, app)
        self.db = UserDatabase()
        self.register_title = ft.Text("Register", size=30, weight=ft.FontWeight.BOLD)  # Заголовок экрана регистрации
        self.login_field = ft.TextField(label="Login", width=280)  # Поле ввода логина
        self.email_field = ft.TextField(label="Email", width=280)  # Поле ввода email
        self.password_field = ft.TextField(
            label="Password",
            password=True,
            can_reveal_password=True,
            width=280,
        )  # Поле ввода пароля
        self.register_button = ft.ElevatedButton(
            text="Register",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.register_clicked,
        )  # Кнопка регистрации
        self.go_back_button = ft.TextButton(
            text="Go back",
            on_click=self.go_back,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
        )  # Кнопка возврата на экран входа
        self.logo_text = ft.Text(
            "Streamlitify",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )  # Логотип приложения

    def go_back(self, e):
        """
        Возвращает пользователя на экран входа.
        """
        self.app.show_screen("signin")  # Показывает экран входа

    def register_clicked(self, e):
        """
        Обрабатывает нажатие на кнопку регистрации.
        """
        login = self.login_field.value.lower()  # Получает логин пользователя
        email = self.email_field.value.lower()  # Получает email пользователя
        password = self.password_field.value  # Получает пароль пользователя

        if not self.db.validate_password(password):
            # Проверяет, что пароль содержит минимум 8 символов
            self.page.snack_bar = ft.SnackBar(ft.Text("Password must be at least 8 characters long"))
            self.page.snack_bar.open = True
            self.page.update()
            return

        if not self.is_valid_email(email):
            # Проверяет формат email
            self.page.snack_bar = ft.SnackBar(ft.Text("Invalid email format"))
            self.page.snack_bar.open = True
            self.page.update()
            return

        if self.db.user_exists(email) or self.db.user_exists(login):
            # Проверяет, существует ли пользователь с таким email или логином
            self.page.snack_bar = ft.SnackBar(ft.Text("User with this email or login already exists"))
            self.page.snack_bar.open = True
            self.page.update()
            return

        if self.db.add_user(login, email, password):
            # Добавляет пользователя в базу данных
            self.app.login = login
            self.app.email = email
            self.clear_fields()
            self.app.show_screen("mainmenu")
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Failed to register user"))
            self.page.snack_bar.open = True
            self.page.update()

    @staticmethod
    def is_valid_email(email):
        """
        Проверяет, что email имеет правильный формат.
        """
        # Регулярное выражение для проверки формата email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # Проверка на соответствие паттерну и отсутствие последовательных точек в домене
        if re.match(pattern, email) and '..' not in email.split('@')[1]:
            return True
        return False

    def clear_fields(self):
        """
        Очищает поля ввода на экране регистрации.
        """
        self.login_field.value = ""
        self.email_field.value = ""
        self.password_field.value = ""
        self.page.update()

    def build(self):
        """
        Строит и возвращает интерфейс экрана регистрации.
        """
        register_container = ft.Container(
            content=ft.Column(
                [
                    self.register_title,
                    self.login_field,
                    self.email_field,
                    self.password_field,
                    self.register_button,
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            border_radius=10,
            border=ft.border.all(color=ft.colors.PURPLE, width=2),
            padding=20,
            width=320,
            height=500,
        )

        register_page_container = ft.Column(
            [
                ft.Row(
                    [
                        self.logo_text,
                        ft.Container(expand=True),
                        self.go_back_button,
                    ]
                ),
                ft.Container(
                    content=register_container,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Row(
                    [
                        ft.Container(expand=True),
                        self.theme_button,
                    ]
                ),
            ],
            expand=True,
        )

        return register_page_container
