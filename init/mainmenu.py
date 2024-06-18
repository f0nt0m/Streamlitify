import flet as ft
from init.basescreen import BaseScreen


class MainMenuScreen(BaseScreen):
    """
    Экран главного меню.
    """

    def __init__(self, page, app):
        """
        Инициализирует экран главного меню.
        """
        super().__init__(page, app)
        self.signout_button = ft.TextButton(
            text="Sign out",
            on_click=self.signout,  # Метод, вызываемый при нажатии кнопки выхода
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
        )
        self.profile_button = ft.IconButton(
            icon=ft.icons.ACCOUNT_CIRCLE,  # Иконка профиля
            icon_color=ft.colors.PURPLE,  # Цвет иконки
            on_click=self.profile_clicked,  # Метод, вызываемый при нажатии кнопки профиля
        )
        self.menu_title = ft.Text(f"Main Menu", size=30, weight=ft.FontWeight.BOLD)
        self.menu_subtitle = ft.Text(f"Select from the list below:", size=20)
        self.theory_button = ft.ElevatedButton(
            text="Theory",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.theory_clicked,  # Метод, вызываемый при нажатии кнопки теории
        )
        self.test_button = ft.ElevatedButton(
            text="Test",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.test_clicked,  # Метод, вызываемый при нажатии кнопки теста
        )
        self.simulator_button = ft.ElevatedButton(
            text="Simulator",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=280,
            on_click=self.simulator_clicked,  # Метод, вызываемый при нажатии кнопки симулятора
        )
        self.logo_text = ft.Text(
            "Streamlitify",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )

    def signout(self, e):
        """
        Выполняет выход из аккаунта пользователя.
        """
        self.app.screens["signin"].clear_fields()  # Очищаем поля ввода на экране входа
        self.app.show_screen("main")  # Показ главного экрана

    def profile_clicked(self, e):
        """
        Переключает приложение на экран профиля пользователя.
        """
        self.app.show_screen("profile")  # Показ экрана профиля

    def test_clicked(self, e):
        """
        Переключает приложение на экран тестирования.
        """
        self.app.show_screen("test1")  # Показ экрана теста

    def theory_clicked(self, e):
        """
        Переключает приложение на экран теоретических материалов.
        """
        self.app.show_screen("theory1")  # Показ экрана теории

    def simulator_clicked(self, e):
        """
        Переключает приложение на экран симулятора кода.
        """
        self.app.show_screen("simulator1")  # Показ экрана симулятора

    def build(self):
        """
        Строит и возвращает интерфейс экрана главного меню.
        """
        main_menu_container = ft.Container(
            content=ft.Column(
                [
                    self.menu_title,
                    self.menu_subtitle,
                    self.theory_button,
                    self.test_button,
                    self.simulator_button,
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
                    content=main_menu_container,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Row(
                    [
                        self.profile_button,  # Кнопка профиля
                        ft.Container(expand=True),
                        self.theme_button,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
            ],
            expand=True,
        )

        return main_menu_page_container
