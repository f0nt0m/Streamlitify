import flet as ft
import json
import random
from init.basescreen import BaseScreen

class TestScreen1(BaseScreen):
    """
    Экран тестирования с вопросами и вариантами ответов.
    """
    def __init__(self, page, app):
        """
        Инициализирует экран тестирования.
        """
        super().__init__(page, app)
        self.test_title = ft.Text(size=30, weight=ft.FontWeight.BOLD)  # Заголовок экрана тестирования
        self.options_text = ft.Text("Options:", size=20, color=ft.colors.PURPLE)  # Текст "Options:"
        self.question = ft.Text(size=22)  # Текст вопроса
        self.question_counter = ft.Text(size=18, color=ft.colors.GREY)  # Текст с номером вопроса
        self.option1_button = ft.ElevatedButton(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=600,
            on_click=lambda e: self.check_answer(0)  # Обработчик нажатия на кнопку 1
        )
        self.option2_button = ft.ElevatedButton(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=600,
            on_click=lambda e: self.check_answer(1)  # Обработчик нажатия на кнопку 2
        )
        self.option3_button = ft.ElevatedButton(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=600,
            on_click=lambda e: self.check_answer(2)  # Обработчик нажатия на кнопку 3
        )
        self.next_question_button = ft.TextButton(
            text="To the next question",
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            on_click=self.next_question,
            disabled=True  # Изначально кнопка "Next" неактивна
        )
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
        self.correct_option = None  # Индекс правильного варианта ответа
        self.question_index = 0  # Индекс текущего вопроса
        self.selected_questions = []  # Список выбранных для теста вопросов
        self.correct_answers = 0  # Счетчик правильных ответов
        self.load_test_content()  # Загрузка вопросов из JSON-файла

    def load_test_content(self):
        """
        Загружает вопросы из JSON-файла.
        """
        with open("text/test.json", "r") as file:
            test_data = json.load(file)["test"]  # Загружает данные из JSON-файла
        self.selected_questions = random.sample(test_data, 20)  # Выбирает случайные 20 вопросов из JSON-файла
        self.display_question()  # Выводит первый вопрос

    def display_question(self):
        """
        Выводит текущий вопрос на экран.
        """
        question_data = self.selected_questions[self.question_index]  # Получает данные текущего вопроса
        self.test_title.value = question_data["title"]  # Устанавливает заголовок вопроса
        self.question.value = question_data["question"]  # Устанавливает текст вопроса

        # Перемешивает варианты ответов в случайном порядке
        options = question_data["options"]
        correct_option = question_data["correct_option"]
        options_with_index = list(enumerate(options))
        random.shuffle(options_with_index)

        # Сохраняет индекс правильного ответа
        self.correct_option = [index for index, (i, opt) in enumerate(options_with_index) if i == correct_option][0]

        # Присваивает варианты ответов кнопкам
        self.option1_button.text = options_with_index[0][1]
        self.option2_button.text = options_with_index[1][1]
        self.option3_button.text = options_with_index[2][1]

        self.question_counter.value = f"Question {self.question_index + 1} of 20"  # Обновляет номер вопроса
        self.reset_buttons()  # Сбрасывает состояние кнопок

    def reset_buttons(self):
        """
        Сбрасывает состояние кнопок, делая их активными.
        """
        self.option1_button.disabled = False
        self.option2_button.disabled = False
        self.option3_button.disabled = False
        self.option1_button.bgcolor = ft.colors.PURPLE
        self.option2_button.bgcolor = ft.colors.PURPLE
        self.option3_button.bgcolor = ft.colors.PURPLE
        self.next_question_button.disabled = True
        self.page.update()

    def check_answer(self, selected_option):
        """
        Проверяет выбранный пользователем вариант ответа.
        """
        if selected_option == self.correct_option:  # Если ответ правильный
            self.page.snack_bar = ft.SnackBar(ft.Text("You chose correct answer!"))  # Выводит сообщение об успешном решении
            self.correct_answers += 1  # Увеличивает счетчик правильных ответов
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("You chose incorrect answer!"))  # Выводит сообщение о неверном решении

        # Деактивирует кнопки выбора ответов
        self.option1_button.disabled = True
        self.option2_button.disabled = True
        self.option3_button.disabled = True

        # Изменяет цвет кнопки, соответствующей выбранному варианту ответа
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

        self.next_question_button.disabled = False  # Активирует кнопку "Next"
        self.page.snack_bar.open = True  # Показывает сообщение
        self.page.update()  # Обновляет страницу

    def next_question(self, e):
        """
        Переходит к следующему вопросу.
        """
        self.question_index += 1  # Увеличивает индекс текущего вопроса
        if self.question_index < 20:  # Если есть следующий вопрос
            self.display_question()  # Выводит следующий вопрос
        else:
            self.app.show_screen("testresults")  # Показывает экран с результатами теста
            self.app.screens["testresults"].set_results(self.correct_answers, 20)  # Передает результаты на экран с результатами

    def go_back(self, e):
        """
        Возвращает пользователя в главное меню.
        """
        self.reset_test()  # Сбрасывает тест
        self.app.show_screen("mainmenu")  # Показывает главное меню

    def reset_test(self):
        """
        Сбрасывает тест в исходное состояние.
        """
        self.question_index = 0  # Сбрасывает индекс текущего вопроса
        self.correct_answers = 0  # Сбрасывает счетчик правильных ответов
        self.load_test_content()  # Загружает вопросы из JSON-файла

    def build(self):
        """
        Строит и возвращает интерфейс экрана тестирования.
        """
        test_container = ft.Container(
            content=ft.Column(
                [
                    self.test_title,  # Заголовок теста
                    ft.Text("Choose the right answer", size=20),  # Инструкция по выбору ответа
                    ft.Container(height=10),  # Добавляет отступ
                    ft.Row(
                        [self.question],  # Выводит текст вопроса
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    self.question_counter,  # Выводит номер вопроса
                    ft.Container(height=30),  # Добавляет отступ
                    ft.Column(
                        [
                            self.options_text,  # Выводит текст "Options:"
                            ft.Container(height=10),  # Добавляет отступ
                            ft.Row(
                                [self.option1_button],  # Выводит кнопку 1
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                [self.option2_button],  # Выводит кнопку 2
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                [self.option3_button],  # Выводит кнопку 3
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    self.next_question_button,  # Выводит кнопку "Next"
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
                        self.logo_text,  # Логотип приложения
                        ft.Container(expand=True),  # Растягиваем пустой контейнер
                        self.go_back_button,  # Кнопка возврата в главное меню
                    ]
                ),
                ft.Container(
                    content=test_container,
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
        return test_page_container