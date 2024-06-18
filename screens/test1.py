import flet as ft
import json
import random
from init.basescreen import BaseScreen

class TestScreen1(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.test_title = ft.Text(size=30, weight=ft.FontWeight.BOLD)
        self.options_text = ft.Text("Options:", size=20, color=ft.colors.PURPLE)
        self.question = ft.Text(size=22)
        self.question_counter = ft.Text(size=18, color=ft.colors.GREY)
        self.option1_button = ft.ElevatedButton(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=600,
            on_click=lambda e: self.check_answer(0)
        )
        self.option2_button = ft.ElevatedButton(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=600,
            on_click=lambda e: self.check_answer(1)
        )
        self.option3_button = ft.ElevatedButton(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=600,
            on_click=lambda e: self.check_answer(2)
        )
        self.next_question_button = ft.TextButton(
            text="To the next question",
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            on_click=self.next_question,
            disabled=True
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
        self.correct_option = None
        self.question_index = 0
        self.selected_questions = []
        self.correct_answers = 0
        self.load_test_content()

    def load_test_content(self):
        with open("text/test.json", "r") as file:
            test_data = json.load(file)["test"]

        self.selected_questions = random.sample(test_data, 20)
        self.display_question()

    def display_question(self):
        question_data = self.selected_questions[self.question_index]
        self.test_title.value = question_data["title"]
        self.question.value = question_data["question"]
        self.option1_button.text = question_data["options"][0]
        self.option2_button.text = question_data["options"][1]
        self.option3_button.text = question_data["options"][2]
        self.correct_option = question_data["correct_option"]
        self.question_counter.value = f"Question {self.question_index + 1} of 20"
        self.reset_buttons()

    def reset_buttons(self):
        self.option1_button.disabled = False
        self.option2_button.disabled = False
        self.option3_button.disabled = False
        self.option1_button.bgcolor = ft.colors.PURPLE
        self.option2_button.bgcolor = ft.colors.PURPLE
        self.option3_button.bgcolor = ft.colors.PURPLE
        self.next_question_button.disabled = True
        self.page.update()

    def check_answer(self, selected_option):
        if selected_option == self.correct_option:
            self.page.snack_bar = ft.SnackBar(ft.Text("You chose correct answer!"))
            self.correct_answers += 1
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("You chose incorrect answer!"))

        self.option1_button.disabled = True
        self.option2_button.disabled = True
        self.option3_button.disabled = True

        if selected_option == 0:
            self.option1_button.bgcolor = ft.colors.PURPLE
            self.option2_button.bgcolor = ft.colors.GREY
            self.option3_button.bgcolor = ft.colors.GREY
        elif selected_option == 1:
            self.option1_button.bgcolor = ft.colors.GREY
            self.option2_button.bgcolor = ft.colors.PURPLE
            self.option3_button.bgcolor = ft.colors.GREY
        else:
            self.option1_button.bgcolor = ft.colors.GREY
            self.option2_button.bgcolor = ft.colors.GREY
            self.option3_button.bgcolor = ft.colors.PURPLE

        self.next_question_button.disabled = False
        self.page.snack_bar.open = True
        self.page.update()

    def next_question(self, e):
        self.question_index += 1
        if self.question_index < 20:
            self.display_question()
        else:
            self.app.show_screen("testresults")
            self.app.screens["testresults"].set_results(self.correct_answers, 20)

    def go_back(self, e):
        self.reset_test()
        self.app.show_screen("mainmenu")

    def reset_test(self):
        self.question_index = 0
        self.correct_answers = 0
        self.load_test_content()

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
                    self.question_counter,
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
            width=900,
            height=600,
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
