import flet as ft
from basescreen import BaseScreen


class MainScreen(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.welcome_text = ft.Text(
            "", size=40, text_align=ft.TextAlign.CENTER
        )  # Increased size
        self.app_name_text = ft.Text(
            "", size=60, weight=ft.FontWeight.BOLD, color=ft.colors.PURPLE
        )  # Increased size
        self.subtitle_text = ft.Text(
            "", size=25, text_align=ft.TextAlign.CENTER
        )  # Increased size
        self.start_button = ft.ElevatedButton(
            text="",
            on_click=self.start_clicked,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=200,
            height=50,
        )  # Increased size
        self.exit_button = ft.TextButton(
            text="",
            on_click=lambda e: page.window_close(),
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            height=40,
        )  # Increased size
        self.contact_button = ft.TextButton(
            text="",
            on_click=lambda e: page.launch_url("https://t.me/f0ntt0m"),
            icon=ft.icons.SEND,
            icon_color=ft.colors.PURPLE,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            height=40,
        )  # Increased size
        self.support_button = ft.TextButton(
            text="",
            on_click=lambda e: page.launch_url(
                "https://www.tinkoff.ru/cf/188uzPH7nwb"
            ),
            icon=ft.icons.SEARCH,
            icon_color=ft.colors.PURPLE,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            height=40,
        )  # Increased size

    def start_clicked(self, e):
        self.app.show_screen("signin")

    def update_texts(self):
        self.welcome_text.value = self.app.translations[self.app.language][
            "welcome"
        ]
        self.app_name_text.value = self.app.translations[self.app.language][
            "app_name"
        ]
        self.subtitle_text.value = self.app.translations[self.app.language][
            "subtitle"
        ]
        self.start_button.text = self.app.translations[self.app.language][
            "start"
        ]
        self.exit_button.text = self.app.translations[self.app.language][
            "exit"
        ]
        self.contact_button.text = self.app.translations[self.app.language][
            "contact"
        ]
        self.support_button.text = self.app.translations[self.app.language][
            "support"
        ]
        self.language_selector.value = self.app.language
        self.page.update()

    def build(self):
        # Создание контейнера для центрирования элементов
        main_container = ft.Column(
            [
                self.welcome_text,
                self.app_name_text,
                self.subtitle_text,
                ft.Container(
                    height=20
                ),  # Spacer to add some space between subtitle and buttons
                self.start_button,
                self.exit_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        # Контейнер для контактных кнопок
        footer_container = ft.Row(
            [
                self.contact_button,
                ft.Container(expand=True),
                self.support_button,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.END,
        )

        # Обернем основной контейнер в другой контейнер с растягиванием на всю доступную площадь
        centered_container = ft.Container(
            content=main_container,
            alignment=ft.alignment.center,
            expand=True,
        )

        # Обернем в контейнер с кнопками вверху и внизу
        full_container = ft.Column(
            [
                ft.Row(
                    [
                        self.language_selector,
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
