import flet as ft
from init.basescreen import BaseScreen


class TestScreen1(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.test_title = ft.Text("Test", size=30, weight=ft.FontWeight.BOLD)
        self.options_text = ft.Text("Options:", size=20, color=ft.colors.PURPLE)
        self.question = ft.Text("What is the primary purpose of the Streamlit framework?", size=22)
        self.option1_button = ft.ElevatedButton(
            text="To build web applications for data science and machine learning",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=500,
        )
        self.option2_button = ft.ElevatedButton(
            text="To create static websites with HTML and CSS",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=500,
        )
        self.option3_button = ft.ElevatedButton(
            text="To manage databases and perform SQL queries",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=500,
        )
        self.next_question_button = ft.TextButton(
            text="To the next question",
            style=ft.ButtonStyle(color=ft.colors.PURPLE)
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

    def go_back(self, e):
        self.app.show_screen("mainmenu")

    def build(self):
        test_container = ft.Container(
            content=ft.Column(
                [
                    self.test_title,
                    ft.Text("Choose the right answer", size=20),
                    ft.Container(height=10),
                    ft.Row(
                        [self.question],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Container(height=30),
                    ft.Column(
                        [
                            self.options_text,
                            ft.Container(height=10),
                            ft.Row(
                                [self.option1_button],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                [self.option2_button],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                [self.option3_button],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    self.next_question_button,
                ],
                spacing=15,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=10,
            border=ft.border.all(color=ft.colors.PURPLE, width=2),
            padding=20,
            expand=True,
            width=650,
            height=500,
        )

        test_page_container = ft.Column(
            [
                ft.Row(
                    [
                        self.logo_text,
                        ft.Container(expand=True),
                        self.go_back_button,
                    ]
                ),
                ft.Container(
                    content=test_container,
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
        return test_page_container
