import flet as ft
from init.basescreen import BaseScreen
from init.database import UserDatabase

class ProfileScreen(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.db = UserDatabase()
        self.user_icon = ft.Icon(name=ft.icons.ACCOUNT_CIRCLE, size=50, color=ft.colors.PURPLE)
        self.profile_title = ft.Text("User Profile", size=30, weight=ft.FontWeight.BOLD)
        self.login_text = ft.Text(size=16)
        self.email_text = ft.Text(size=16)
        self.back_button = ft.ElevatedButton(
            text="Back to Main Menu",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=200,
            on_click=self.go_back,
        )

    def go_back(self, e):
        self.app.show_screen("mainmenu")

    def build(self):
        user_data = self.db.get_user_data(self.app.login)
        self.login_text.value = f"Login: {user_data['login']}"
        self.email_text.value = f"Email: {user_data['email']}"

        profile_container = ft.Container(
            content=ft.Column(
                [
                    self.user_icon,
                    ft.Container(height=20),  # Добавляем отступ
                    self.profile_title,
                    ft.Container(height=20),  # Добавляем отступ
                    self.login_text,
                    self.email_text,
                    ft.Container(height=20),  # Добавляем отступ
                    self.back_button,
                ],
                width=400,
                height=300,
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=10,
            border=ft.border.all(color=ft.colors.PURPLE, width=2),
            padding=20,
        )

        profile_page_container = ft.Column(
            [
                ft.Container(
                    content=profile_container,
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
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        return profile_page_container
