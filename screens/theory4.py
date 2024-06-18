import flet as ft
from init.basescreen import BaseScreen
import json

class TheoryScreen4(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.theory_title = ft.Text("Deploying Streamlit Apps", size=30, weight=ft.FontWeight.BOLD)
        self.theory_text = ft.Column(width=600, spacing=0)
        self.next_topic_button = ft.ElevatedButton(
            text="To the next topic",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=200,
            on_click=self.go_to_next_topic
        )
        self.go_back_button = ft.TextButton(
            text="Return to main menu",
            on_click=self.go_back,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
        )
        self.logo_text = ft.Text(
            "Streamlitify",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )
        self.scroll_container = None
        self.load_theory_content()

    def load_theory_content(self):
        with open("text/theory.json", "r") as file:
            theory_data = json.load(file)["theory4"]

        content = []
        for item in theory_data:
            if item.startswith("CODE:"):
                content.append(self.create_code_block(item[5:]))
            else:
                content.append(ft.Text(item, size=16))

        self.theory_text.controls.clear()
        self.theory_text.controls.extend(content)

    def go_back(self, e):
        self.app.show_screen("mainmenu")

    def go_to_next_topic(self, e):
        self.app.show_screen("theory5")

    def copy_to_clipboard(self, e, text):
        self.page.set_clipboard(text)
        self.page.snack_bar = ft.SnackBar(ft.Text("Copied to clipboard!"))
        self.page.snack_bar.open = True
        self.page.update()

    def create_code_block(self, code_text):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Text(
                            code_text,
                            font_family="Courier",
                            size=16,
                            color=ft.colors.WHITE,
                        ),
                        expand=True,
                    ),
                    ft.IconButton(
                        icon=ft.icons.CONTENT_COPY,
                        on_click=lambda e: self.copy_to_clipboard(e, code_text),
                        tooltip="Copy to clipboard",
                        icon_color=ft.colors.WHITE,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=ft.colors.BLACK,
            padding=10,
            border_radius=5,
            margin=ft.margin.symmetric(vertical=5),  # Добавлен вертикальный отступ между блоками
        )

    def build(self):
        self.scroll_container = ft.Container(
            content=ft.Column(
                [
                    self.theory_title,
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=self.theory_text,
                                    expand=True,
                                )
                            ],
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,  # Включили автоматический скроллинг
                        ),
                        expand=True,
                    ),
                    self.next_topic_button,
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=10,
            border=ft.border.all(color=ft.colors.PURPLE, width=2),
            padding=10,
            expand=True,
            width=750,
        )

        theory_page_container = ft.Column(
            [
                ft.Row(
                    [
                        self.logo_text,
                        ft.Container(expand=True),
                        self.go_back_button,
                    ]
                ),
                ft.Container(
                    content=self.scroll_container,
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
        return theory_page_container
