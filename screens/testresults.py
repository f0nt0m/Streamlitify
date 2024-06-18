import flet as ft
from init.basescreen import BaseScreen
from init.database import UserDatabase


class TestResultsScreen(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.results_title = ft.Text("Test Results", size=30, weight=ft.FontWeight.BOLD)
        self.correct_answers_text = ft.Text(size=20)
        self.percentage_text = ft.Text(size=20)
        self.grade_text = ft.Text(size=20)
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
        self.app.screens["test1"].reset_test()

    def build(self):
        results_container = ft.Container(
            content=ft.Column(
                [
                    self.results_title,
                    self.correct_answers_text,
                    self.percentage_text,
                    self.grade_text,
                ],
                spacing=15,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=10,
            border=ft.border.all(color=ft.colors.PURPLE, width=2),
            padding=20,
            expand=True,
            width=650,
            height=500,
        )

        results_page_container = ft.Column(
            [
                ft.Row(
                    [
                        self.logo_text,
                        ft.Container(expand=True),
                        self.go_back_button,
                    ]
                ),
                ft.Container(
                    content=results_container,
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
        return results_page_container

    def set_results(self, correct_answers, total_questions):
        self.correct_answers_text.value = f"Correct Answers: {correct_answers} / {total_questions}"
        percentage = (correct_answers / total_questions) * 100
        self.percentage_text.value = f"Percentage: {percentage:.2f}%"

        # Пятибальная шкала
        if percentage >= 90:
            grade = "5"
        elif percentage >= 80:
            grade = "4"
        elif percentage >= 70:
            grade = "3"
        elif percentage >= 60:
            grade = "2"
        else:
            grade = "1"

        self.grade_text.value = f"Grade: {grade}"
        self.page.update()

        # Сохранение результатов в БД
        user_id = self.app.current_user_id
        db = UserDatabase()
        db.add_test_result(user_id, correct_answers, total_questions)
        db.close()
