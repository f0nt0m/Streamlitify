import flet as ft
from basescreen import BaseScreen


class MainMenuScreen(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.username = app.username  # Получаем никнейм пользователя
        self.signout_button = ft.TextButton(
            text="",
            on_click=self.signout,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
        )
        self.menu_title = ft.Text(f"", size=30, weight=ft.FontWeight.BOLD)
        self.menu_subtitle = ft.Text(f"", size=20)
        self.theory_button = ft.ElevatedButton(
            text="",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.theory_clicked,
        )
        self.test_button = ft.ElevatedButton(
            text="",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.test_clicked,
        )
        self.simulator_button = ft.ElevatedButton(
            text="",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.simulator_clicked,  # Add on_click for Simulator button
        )
        self.logo_text = ft.Text(
            "Streamlitify",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )

        # Создаем greeting_text здесь
        self.greeting_text = ft.Text(
            spans=[
                ft.TextSpan(
                    text=f"{self.app.translations[self.app.language]['signed_in_as']} "
                ),
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
        self.app.show_screen("test")

    def theory_clicked(self, e):
        self.app.show_screen("theory")

    def simulator_clicked(self, e):
        self.app.show_screen("simulator")  # Show the Simulator screen

    def update_texts(self):
        # Обновляем текст здесь
        self.username = (
            self.app.username
        )  # Получаем актуальный никнейм пользователя
        self.greeting_text.spans[0].text = self.app.translations[
            self.app.language
        ]["signed_in_as"]
        self.greeting_text.spans[1].text = (
            self.username.lower()
        )  # Обновляем никнейм пользователя
        self.signout_button.text = self.app.translations[self.app.language][
            "signout"
        ]
        self.menu_title.value = self.app.translations[self.app.language][
            "main_menu"
        ]
        self.menu_subtitle.value = self.app.translations[self.app.language][
            "main_menu_select"
        ]
        self.theory_button.text = self.app.translations[self.app.language][
            "theory"
        ]
        self.test_button.text = self.app.translations[self.app.language][
            "test"
        ]
        self.simulator_button.text = self.app.translations[self.app.language][
            "simulator"
        ]
        self.language_selector.value = self.app.language
        self.page.update()

    def build(self):
        main_menu_container = ft.Container(
            content=ft.Column(
                [
                    self.menu_title,
                    self.menu_subtitle,
                    self.theory_button,
                    self.test_button,
                    self.simulator_button,  # Include Simulator button
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
                        self.language_selector,
                        ft.Container(expand=True),
                        self.theme_button,
                    ]
                ),
            ],
            expand=True,
        )

        return main_menu_page_container
