import flet as ft
from init.basescreen import BaseScreen


class TestScreen(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.test_title = ft.Text("", size=30, weight=ft.FontWeight.BOLD)
        self.options_text = ft.Text(
            "", size=20, color=ft.colors.PURPLE
        )  # Increased size
        self.question = ft.Text("", size=22)  # Increased size
        self.option1_button = ft.ElevatedButton(
            text="",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=500,
        )
        self.option2_button = ft.ElevatedButton(
            text="",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=500,
        )
        self.option3_button = ft.ElevatedButton(
            text="",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=500,
        )
        self.next_question_button = ft.TextButton(
            text="", style=ft.ButtonStyle(color=ft.colors.PURPLE)
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
        self.app.show_screen("mainmenu")

    def update_texts(self):
        self.test_title.value = self.app.translations[self.app.language][
            "test"
        ]
        self.options_text.value = self.app.translations[self.app.language][
            "options"
        ]
        self.question.value = self.app.translations[self.app.language][
            "primary_purpose_question"
        ]
        self.option1_button.text = self.app.translations[self.app.language][
            "primary_purpose_option1"
        ]
        self.option2_button.text = self.app.translations[self.app.language][
            "primary_purpose_option2"
        ]
        self.option3_button.text = self.app.translations[self.app.language][
            "primary_purpose_option3"
        ]
        self.next_question_button.text = self.app.translations[
            self.app.language
        ]["next_question"]
        self.go_back_button.text = self.app.translations[self.app.language][
            "return_to_main_menu"
        ]
        self.language_selector.value = self.app.language
        self.page.update()

    def build(self):
        test_container = ft.Container(
            content=ft.Column(
                [
                    self.test_title,
                    ft.Text(
                        self.app.translations[self.app.language][
                            "choose_right_answer"
                        ],
                        size=20,
                    ),
                    ft.Container(height=10),
                    # Spacer to add some space between "Choose the right answer" and the question
                    ft.Row(
                        [self.question],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),  # Centered question
                    ft.Container(
                        height=30
                    ),  # Spacer to add some space between the question and the "Options" label
                    ft.Column(
                        [
                            self.options_text,  # "Options:" label
                            ft.Container(
                                height=10
                            ),  # Spacer to add some space between Options label and buttons
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
            expand=True,  # <--- Added expand=True
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
                        self.language_selector,
                        ft.Container(expand=True),
                        self.theme_button,
                    ]
                ),
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        return test_page_container
