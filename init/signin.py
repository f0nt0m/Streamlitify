import flet as ft
from init.basescreen import BaseScreen
from init.database import UserDatabase


class SignInScreen(BaseScreen):
    """
    Экран входа в аккаунт пользователя.
    """

    def __init__(self, page, app):
        """
        Инициализирует экран входа.
        """
        super().__init__(page, app)
        self.db = UserDatabase()
        self.signin_title = ft.Text("Sign in", size=30, weight=ft.FontWeight.BOLD)  # Заголовок экрана входа
        self.login_field = ft.TextField(label="Login or email", width=280)  # Поле ввода логина или email
        self.password_field = ft.TextField(
            label="Password",
            password=True,
            can_reveal_password=True,
            width=280,
        )  # Поле ввода пароля
        self.signin_button = ft.ElevatedButton(
            text="Sign in",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.signin_clicked,
        )  # Кнопка входа
        self.register_text = ft.Text(
            spans=[
                ft.TextSpan(text="New to Streamlitify? "),
                ft.TextSpan(
                    text="Register",
                    style=ft.TextStyle(color=ft.colors.PURPLE),
                    on_click=self.register_clicked,
                ),
            ]
        )  # Текст с предложением зарегистрироваться
        self.go_back_button = ft.TextButton(
            text="Go back",
            on_click=self.go_back,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
        )  # Кнопка возврата на главный экран
        self.logo_text = ft.Text(
            "Streamlitify",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )  # Логотип приложения

    def go_back(self, e):
        """
        Возвращает пользователя на главный экран.
        """
        self.app.show_screen("main")  # Показывает главный экран

    def register_clicked(self, e):
        """
        Переключает приложение на экран регистрации.
        """
        self.app.show_screen("register")  # Показывает экран регистрации

    def signin_clicked(self, e):
        """
        Обрабатывает нажатие на кнопку входа.
        """
        login_or_email = self.login_field.value  # Получает логин или email
        password = self.password_field.value  # Получает пароль
        user_id = self.db.authenticate_user(login_or_email, password)  # Аутентифицирует пользователя
        if user_id:
            user_data = self.db.get_user_data(login_or_email)  # Получает данные пользователя
            self.app.current_user_id = user_id  # Сохраняет идентификатор пользователя
            self.app.login = user_data["login"]  # Сохраняет логин пользователя
            self.app.email = user_data["email"]  # Сохраняет email пользователя
            self.app.show_screen("mainmenu")  # Показывает главное меню
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Invalid credentials"))
            self.page.snack_bar.open = True
            self.page.update()

    def clear_fields(self):
        """
        Очищает поля ввода на экране входа.
        """
        self.login_field.value = ""
        self.password_field.value = ""
        self.page.update()

    def build(self):
        """
        Строит и возвращает интерфейс экрана входа.
        """
        signin_container = ft.Container(
            content=ft.Column(
                [
                    self.signin_title,
                    self.login_field,
                    self.password_field,
                    self.signin_button,
                    self.register_text,
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            border_radius=10,
            border=ft.border.all(color=ft.colors.PURPLE, width=2),
            padding=20,
            width=320,
            height=450,
        )

        signin_page_container = ft.Column(
            [
                ft.Row(
                    [
                        self.logo_text,
                        ft.Container(expand=True),
                        self.go_back_button,
                    ]
                ),
                ft.Container(
                    content=signin_container,
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

        return signin_page_container
