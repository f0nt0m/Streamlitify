import flet as ft
from init.basescreen import BaseScreen


class MainMenuScreen(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.username = app.username  # Получаем никнейм пользователя
        self.signout_button = ft.TextButton(
            text="Sign out",
            on_click=self.signout,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
        )
        self.menu_title = ft.Text(f"Main Menu", size=30, weight=ft.FontWeight.BOLD)
        self.menu_subtitle = ft.Text(f"Select from the list below:", size=20)
        self.theory_button = ft.ElevatedButton(
            text="Theory",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.theory_clicked,
        )
        self.test_button = ft.ElevatedButton(
            text="Test",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.test_clicked,
        )
        self.simulator_button = ft.ElevatedButton(
            text="Simulator",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.simulator_clicked,
        )
        self.logo_text = ft.Text(
            "Streamlitify",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )

        self.greeting_text = ft.Text(
            spans=[
                ft.TextSpan(text=f"You have signed in as "),
                ft.TextSpan(
                    text=f"{self.username}",
                    style=ft.TextStyle(color=ft.colors.PURPLE),
                ),
            ],
            text_align=ft.TextAlign.CENTER,
        )

    def signout(self, e):
        self.app.show_screen("main")

    def test_clicked(self, e):
        self.app.show_screen("test1")

    def theory_clicked(self, e):
        self.app.show_screen("theory1")

    def simulator_clicked(self, e):
        self.app.show_screen("simulator1")

    def build(self):
        main_menu_container = ft.Container(
            content=ft.Column(
                [
                    self.menu_title,
                    self.menu_subtitle,
                    self.theory_button,
                    self.test_button,
                    self.simulator_button,
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

        main_menu_page_container = ft.Column(
            [
                ft.Row(
                    [
                        self.logo_text,
                        ft.Container(expand=True),
                        self.signout_button,
                    ]
                ),
                ft.Container(
                    height=20,
                    alignment=ft.alignment.center,
                    content=self.greeting_text,
                ),
                ft.Container(
                    content=main_menu_container,
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

        return main_menu_page_container
