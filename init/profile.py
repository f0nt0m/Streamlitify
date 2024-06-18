import flet as ft
from init.basescreen import BaseScreen
from init.database import UserDatabase


class ProfileScreen(BaseScreen):
    """
    Экран профиля пользователя.
    """

    def __init__(self, page, app):
        """
        Инициализирует экран профиля.
        """
        super().__init__(page, app)
        self.db = UserDatabase()
        self.user_icon = ft.Icon(name=ft.icons.ACCOUNT_CIRCLE, size=50, color=ft.colors.PURPLE)  # Иконка пользователя
        self.profile_title = ft.Text("User Profile", size=30, weight=ft.FontWeight.BOLD)  # Заголовок профиля
        self.login_text = ft.Text(size=16)  # Текст с логином пользователя
        self.email_text = ft.Text(size=16)  # Текст с email пользователя
        self.test_results_text = ft.Text(size=16)  # Текст с результатами теста
        self.simulator_results_text = ft.Text(size=16)  # Текст с результатами симулятора
        self.back_button = ft.ElevatedButton(
            text="Back to Main Menu",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=200,
            on_click=self.go_back,
        )  # Кнопка возврата в главное меню

    def go_back(self, e):
        """
        Возвращает пользователя в главное меню.
        """
        self.app.show_screen("mainmenu")  # Показывает главное меню

    def build(self):
        """
        Строит и возвращает интерфейс экрана профиля.
        """
        user_data = self.db.get_user_data(self.app.login)  # Получает данные пользователя из базы данных
        self.login_text.value = f"Login: {user_data['login']}"  # Устанавливает текст логина
        self.email_text.value = f"Email: {user_data['email']}"  # Устанавливает текст email

        # Получает результаты теста и симулятора из базы данных
        test_results = self.db.get_test_results(self.app.current_user_id)
        simulator_results = self.db.get_simulator_results(self.app.current_user_id)

        if test_results:
            correct_answers, total_questions = test_results[0]
            self.test_results_text.value = f"Test Results: {correct_answers} / {total_questions} correct"
        else:
            self.test_results_text.value = "Test Results: No data available"

        if simulator_results:
            correct_simulators, total_simulators = simulator_results[0]
            self.simulator_results_text.value = f"Simulator Results: {correct_simulators} / {total_simulators} correct"
        else:
            self.simulator_results_text.value = "Simulator Results: No data available"

        profile_container = ft.Container(
            content=ft.Column(
                [
                    self.user_icon,
                    ft.Container(height=20),  # Добавляем отступ
                    self.profile_title,
                    ft.Container(height=20),  # Добавляем отступ
                    self.login_text,
                    self.email_text,
                    self.test_results_text,
                    self.simulator_results_text,
                    ft.Container(height=20),  # Добавляем отступ
                    self.back_button,
                ],
                width=400,
                height=400,
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=10,
            border=ft.border.all(color=ft.colors.PURPLE, width=2),
            padding=20,
        )

        profile_page_container = ft.Column(
            [
                ft.Container(
                    content=profile_container,
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
        return profile_page_container
