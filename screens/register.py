import flet as ft
from basescreen import BaseScreen


class RegisterScreen(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.register_title = ft.Text("", size=30, weight=ft.FontWeight.BOLD)
        self.nickname_field = ft.TextField(label="", width=280)
        self.email_field = ft.TextField(label="", width=280)
        self.password_field = ft.TextField(
            label="", password=True, can_reveal_password=True, width=280
        )
        self.register_button = ft.ElevatedButton(
            text="",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.register_clicked,
        )
        self.go_back_button = ft.TextButton(
            text="",
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
        # Здесь будет логика регистрации
        # После успешной регистрации переход на главный экран
        nickname = self.nickname_field.value
        self.app.username = nickname
        self.app.show_screen("mainmenu")

    def update_texts(self):
        self.register_title.value = self.app.translations[self.app.language][
            "register"
        ]
        self.nickname_field.label = self.app.translations[self.app.language][
            "nickname"
        ]
        self.email_field.label = self.app.translations[self.app.language][
            "email"
        ]
        self.password_field.label = self.app.translations[self.app.language][
            "password"
        ]
        self.register_button.text = self.app.translations[self.app.language][
            "register"
        ]
        self.go_back_button.text = self.app.translations[self.app.language][
            "go_back"
        ]
        self.language_selector.value = self.app.language
        self.page.update()

    def build(self):
        register_container = ft.Container(
            content=ft.Column(
                [
                    self.register_title,
                    self.nickname_field,
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
                        self.language_selector,
                        ft.Container(expand=True),
                        self.theme_button,
                    ]
                ),
            ],
            expand=True,
        )

        return register_page_container
