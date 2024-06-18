import json
import random
import flet as ft
from init.basescreen import BaseScreen


class SimulatorScreen1(BaseScreen):
    """
    Экран симулятора кода для практики.
    """

    def __init__(self, page, app):
        """
        Инициализирует экран симулятора.
        """
        super().__init__(page, app)
        self.page = page
        self.app = app
        self.simulator_data = self.load_simulator_data()  # Загружает данные для симулятора из JSON-файла
        self.current_index = 0  # Индекс текущей задачи
        self.correct_simulators = 0  # Счетчик правильно решенных задач
        self.attempts = {}  # Словарь для отслеживания количества попыток на каждую задачу
        random.shuffle(self.simulator_data)  # Перемешивает задачи в случайном порядке
        self.init_ui()  # Инициализирует элементы интерфейса
        self.load_task()  # Загружает первую задачу

    def load_simulator_data(self):
        """
        Загружает данные для симулятора из JSON-файла.
        """
        with open("text/simulator.json", "r") as file:
            data = json.load(file)
            return data["simulator"]

    def init_ui(self):
        """
        Инициализирует элементы интерфейса экрана симулятора.
        """
        self.simulator_title = ft.Text(size=30, weight=ft.FontWeight.BOLD)  # Заголовок экрана
        self.simulator_description = ft.Text(size=20, weight=ft.FontWeight.NORMAL)  # Описание симулятора
        self.code_snippet = ft.Text(size=16, font_family="monospace", width=600)  # Фрагмент кода с ошибкой
        self.user_input = ft.TextField(label="Your Code", hint_text="Enter corrected code", width=600, multiline=True, height=100)  # Поле ввода для исправления кода
        self.check_button = ft.ElevatedButton(text="Check", color=ft.colors.WHITE, bgcolor=ft.colors.PURPLE, width=250, on_click=self.check_code)  # Кнопка проверки кода
        self.result_text = ft.Text("", size=16)  # Текст с результатом проверки
        self.go_back_button = ft.TextButton(text="Return to main menu", on_click=self.go_back, style=ft.ButtonStyle(color=ft.colors.PURPLE))  # Кнопка возврата в главное меню
        self.next_button = ft.ElevatedButton(text="Next", color=ft.colors.WHITE, bgcolor=ft.colors.PURPLE, width=110, on_click=self.next_task, disabled=True)  # Кнопка перехода к следующей задаче
        self.logo_text = ft.Text("Streamlitify", size=25, weight=ft.FontWeight.BOLD, color=ft.colors.PURPLE)  # Логотип приложения

    def load_task(self):
        """
        Загружает текущую задачу.
        """
        task = self.simulator_data[self.current_index]
        self.simulator_title.value = task["title"]  # Устанавливает заголовок задачи
        self.simulator_description.value = task["description"]  # Устанавливает описание задачи
        self.code_snippet.value = task["code_snippet"]  # Устанавливает фрагмент кода с ошибкой
        self.user_input.value = ""  # Очищает поле ввода
        self.result_text.value = ""  # Очищает текст с результатом проверки
        self.next_button.disabled = True  # Деактивирует кнопку "Next"
        self.attempts[self.current_index] = 0  # Сбрасывает счетчик попыток для текущей задачи
        self.page.update()  # Обновляет страницу

    def go_back(self, e):
        """
        Возвращает пользователя в главное меню.
        """
        self.reset_simulator()  # Сбрасывает симулятор
        self.app.show_screen("mainmenu")  # Показывает главное меню

    def next_task(self, e):
        """
        Переходит к следующей задаче.
        """
        if self.current_index < len(self.simulator_data) - 1:  # Если есть следующая задача
            self.current_index += 1
            self.load_task()  # Загружает следующую задачу
        else:
            self.app.show_screen("simulatorresults")  # Показывает экран с результатами симулятора
            self.app.screens["simulatorresults"].set_results(self.correct_simulators, len(self.simulator_data))  # Передает результаты на экран с результатами

    def prev_task(self, e):
        """
        Переходит к предыдущей задаче.
        """
        if self.current_index > 0:
            self.current_index -= 1
            self.load_task()

    def check_code(self, e):
        """
        Проверяет введенный пользователем код.
        """
        user_code = self.user_input.value  # Получает введенный пользователем код
        correct_code = self.simulator_data[self.current_index]['correct_code']  # Получает правильный код из данных симулятора
        self.attempts[self.current_index] += 1  # Увеличивает счетчик попыток для текущей задачи
        if user_code == correct_code:  # Если код верный
            self.result_text.value = "Correct! You fixed the code!"  # Выводит сообщение об успешном решении
            if self.attempts[self.current_index] == 1:  # Если это первая попытка
                self.correct_simulators += 1  # Увеличивает счетчик правильно решенных задач
            self.next_button.disabled = False  # Активирует кнопку "Next"
        else:
            self.result_text.value = "Oops, try again!"  # Выводит сообщение о неверном решении
        self.page.update()  # Обновляет страницу

    def reset_simulator(self):
        """
        Сбрасывает симулятор в исходное состояние.
        """
        self.current_index = 0  # Сбрасывает индекс текущей задачи
        self.correct_simulators = 0  # Сбрасывает счетчик правильно решенных задач
        self.attempts = {}  # Сбрасывает словарь с количеством попыток
        random.shuffle(self.simulator_data)  # Перемешивает задачи в случайном порядке
        self.load_task()  # Загружает первую задачу

    def build(self):
        """
        Строит и возвращает интерфейс экрана симулятора.
        """
        simulator_container = ft.Container(
            content=ft.Column(
                [
                    self.simulator_title,  # Заголовок симулятора
                    self.simulator_description,  # Описание симулятора
                    ft.Container(
                        content=ft.Column(
                            [
                                self.code_snippet,  # Фрагмент кода с ошибкой
                                self.user_input,  # Поле ввода для исправления кода
                            ],
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=20,
                        expand=True,
                    ),
                    self.check_button,  # Кнопка проверки кода
                    self.result_text,  # Текст с результатом проверки
                    ft.Row(
                        [
                            ft.Container(expand=True),  # Растягиваем пустой контейнер
                            self.next_button,  # Кнопка перехода к следующей задаче
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    ),
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=10,
            border=ft.border.all(color=ft.colors.PURPLE, width=2),
            padding=20,
            expand=True,
            width=750,
            height=600,
        )

        simulator_page_container = ft.Column(
            [
                ft.Row(
                    [
                        self.logo_text,  # Логотип приложения
                        ft.Container(expand=True),  # Растягиваем пустой контейнер
                        self.go_back_button,  # Кнопка возврата в главное меню
                    ]
                ),
                ft.Container(
                    content=simulator_container,
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
        return simulator_page_container
