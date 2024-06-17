import flet as ft
from init.basescreen import BaseScreen
from init.database import UserDatabase


class RegisterScreen(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.db = UserDatabase()
        self.register_title = ft.Text("Register", size=30, weight=ft.FontWeight.BOLD)
        self.login_field = ft.TextField(label="Login", width=280)
        self.email_field = ft.TextField(label="Email", width=280)
        self.password_field = ft.TextField(
            label="Password",
            password=True,
            can_reveal_password=True,
            width=280,
        )
        self.register_button = ft.ElevatedButton(
            text="Register",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.register_clicked,
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
        self.app.show_screen("signin")

    def register_clicked(self, e):
        login = self.login_field.value
        email = self.email_field.value
        password = self.password_field.value

        if not self.db.validate_password(password):
            self.page.snack_bar = ft.SnackBar(ft.Text("Password must be at least 8 characters long"))
            self.page.snack_bar.open = True
            self.page.update()
            return

        if self.db.user_exists(email):
            self.page.snack_bar = ft.SnackBar(ft.Text("User with this email already exists"))
            self.page.snack_bar.open = True
            self.page.update()
            return

        if self.db.add_user(login, email, password):
            self.app.login = login
            self.app.email = email
            self.app.show_screen("mainmenu")
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Failed to register user"))
            self.page.snack_bar.open = True
            self.page.update()

    def build(self):
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
