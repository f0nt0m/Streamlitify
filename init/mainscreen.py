import flet as ft
from init.basescreen import BaseScreen


class MainScreen(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.welcome_text = ft.Text(
            "Welcome to", size=40, text_align=ft.TextAlign.CENTER
        )
        self.app_name_text = ft.Text(
            "Streamlitify",
            size=60,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )
        self.subtitle_text = ft.Text(
            "Unlock the power of data with Streamlitify",
            size=25,
            text_align=ft.TextAlign.CENTER,
        )
        self.start_button = ft.ElevatedButton(
            text="Start Learning",
            on_click=self.start_clicked,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=200,
            height=50,
        )
        self.exit_button = ft.TextButton(
            text="Exit",
            on_click=lambda e: page.window_close(),
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            height=40,
        )
        self.contact_button = ft.TextButton(
            text="Contact me",
            on_click=lambda e: page.launch_url("https://t.me/f0ntt0m"),
            icon=ft.icons.SEND,
            icon_color=ft.colors.PURPLE,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            height=40,
        )
        self.support_button = ft.TextButton(
            text="Support me",
            on_click=lambda e: page.launch_url(
                "https://www.tinkoff.ru/cf/188uzPH7nwb"
            ),
            icon=ft.icons.SEARCH,
            icon_color=ft.colors.PURPLE,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            height=40,
        )
        self.github_button = ft.TextButton(
            text="GitHub",
            on_click=lambda e: page.launch_url("https://github.com/f0nt0m"),
            icon=ft.icons.CODE,
            icon_color=ft.colors.PURPLE,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            height=40,
        )

    def start_clicked(self, e):
        self.app.show_screen("signin")

    def build(self):
        main_container = ft.Column(
            [
                self.welcome_text,
                self.app_name_text,
                self.subtitle_text,
                ft.Container(height=20),
                self.start_button,
                self.exit_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        footer_container = ft.Row(
            [
                self.contact_button,
                ft.Container(expand=True),
                self.support_button,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.END,
        )

        centered_container = ft.Container(
            content=main_container,
            alignment=ft.alignment.center,
            expand=True,
        )

        # Перемещаем github_button сюда
        full_container = ft.Column(
            [
                ft.Row(
                    [
                        self.github_button,  # Кнопка GitHub в левом верхнем углу
                        ft.Container(expand=True),
                        self.theme_button,
                    ]
                ),
                centered_container,
                footer_container,
            ],
            expand=True,
        )

        return full_container
