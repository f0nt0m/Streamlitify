import flet as ft
from init.basescreen import BaseScreen
from init.database import UserDatabase


class SignInScreen(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.db = UserDatabase()
        self.signin_title = ft.Text("Sign in", size=30, weight=ft.FontWeight.BOLD)
        self.login_field = ft.TextField(label="Login or email", width=280)
        self.password_field = ft.TextField(
            label="Password",
            password=True,
            can_reveal_password=True,
            width=280,
        )
        self.signin_button = ft.ElevatedButton(
            text="Sign in",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.signin_clicked,
        )
        self.register_text = ft.Text(
            spans=[
                ft.TextSpan(text="New to Streamlitify? "),
                ft.TextSpan(
                    text="Register",
                    style=ft.TextStyle(color=ft.colors.PURPLE),
                    on_click=self.register_clicked,
                ),
            ]
        )
        self.go_back_button = ft.TextButton(
            text="Go back",
            on_click=self.go_back,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
        )
        self.logo_text = ft.Text(
            "Streamlitify",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )

    def go_back(self, e):
        self.app.show_screen("main")

    def register_clicked(self, e):
        self.app.show_screen("register")

    def signin_clicked(self, e):
        login_or_email = self.login_field.value
        password = self.password_field.value
        if self.db.authenticate_user(login_or_email, password):
            user_data = self.db.get_user_data(login_or_email)
            self.app.login = user_data["login"]
            self.app.email = user_data["email"]
            self.app.show_screen("mainmenu")
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Invalid credentials"))
            self.page.snack_bar.open = True
            self.page.update()

    def clear_fields(self):
        self.login_field.value = ""
        self.password_field.value = ""
        self.page.update()

    def build(self):
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
