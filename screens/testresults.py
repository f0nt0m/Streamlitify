import flet as ft
from init.basescreen import BaseScreen
from init.database import UserDatabase


class TestResultsScreen(BaseScreen):
    """
    Экран с результатами тестирования.
    """

    def __init__(self, page, app):
        """
        Инициализирует экран с результатами.
        """
        super().__init__(page, app)
        self.results_title = ft.Text("Test Results", size=30, weight=ft.FontWeight.BOLD)  # Заголовок экрана с результатами
        self.correct_answers_text = ft.Text(size=20)  # Текст с количеством правильных ответов
        self.percentage_text = ft.Text(size=20)  # Текст с процентом успешных решений
        self.grade_text = ft.Text(size=20)  # Текст с оценкой
        self.go_back_button = ft.TextButton(
            text="Return to main menu",
            on_click=self.go_back,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
        )  # Кнопка возврата в главное меню
        self.logo_text = ft.Text(
            "Streamlitify",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )  # Логотип приложения

    def go_back(self, e):
        """
        Возвращает пользователя в главное меню.
        """
        self.app.show_screen("mainmenu")  # Показывает главное меню
        self.app.screens["test1"].reset_test()  # Сбрасывает тест

    def build(self):
        """
        Строит и возвращает интерфейс экрана с результатами.
        """
        results_container = ft.Container(
            content=ft.Column(
                [
                    self.results_title,  # Заголовок результатов
                    self.correct_answers_text,  # Текст с количеством правильных ответов
                    self.percentage_text,  # Текст с процентом успешных решений
                    self.grade_text,  # Текст с оценкой
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
                        self.logo_text,  # Логотип приложения
                        ft.Container(expand=True),  # Растягиваем пустой контейнер
                        self.go_back_button,  # Кнопка возврата в главное меню
                    ]
                ),
                ft.Container(
                    content=results_container,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Row(
                    [
                        ft.Container(expand=True),  # Растягиваем пустой контейнер
                        self.theme_button,  # Кнопка переключения темы
                    ]
                ),
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        return results_page_container

    def set_results(self, correct_answers, total_questions):
        """
        Устанавливает результаты теста на экран.
        """
        self.correct_answers_text.value = f"Correct Answers: {correct_answers} / {total_questions}"  # Выводит количество правильных ответов
        percentage = (correct_answers / total_questions) * 100  # Рассчитывает процент успешных решений
        self.percentage_text.value = f"Percentage: {percentage:.2f}%"  # Выводит процент успешных решений

        self.grade_text.value = f"Grade: {self.get_grade(percentage)}"  # Выводит оценку на основе процента успешных решений
        self.page.update()  # Обновляет страницу

        # Сохранение результатов в БД
        user_id = self.app.current_user_id
        db = UserDatabase()
        existing_results = db.get_test_results(user_id)
        if existing_results:
            db.update_test_result(user_id, correct_answers, total_questions)
        else:
            db.add_test_result(user_id, correct_answers, total_questions)
        db.close()

    def get_grade(self, percentage):
        """
        Возвращает оценку по пятибалльной шкале на основе процента успешных решений.
        """
        if percentage >= 90:
            return "5"
        elif percentage >= 80:
            return "4"
        elif percentage >= 70:
            return "3"
        elif percentage >= 60:
            return "2"
        else:
            return "1"
