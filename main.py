import flet as ft
from init.mainscreen import MainScreen
from init.signin import SignInScreen
from init.register import RegisterScreen
from init.mainmenu import MainMenuScreen
from init.profile import ProfileScreen
from screens.test1 import TestScreen1
from screens.theory1 import TheoryScreen1
from screens.simulator1 import SimulatorScreen1
from screens.testresults import TestResultsScreen
from screens.simulatorresults import SimulatorResultsScreen


class StreamlitLearnApp:
    """
    Главный класс приложения.
    """

    def __init__(self):
        """
        Инициализирует приложение.
        """
        self.page = None  # Экземпляр страницы Flet
        self.theme_mode = ft.ThemeMode.SYSTEM  # Тема системы по умолчанию
        self.login = None  # Логин пользователя
        self.email = None  # Email пользователя
        self.screens = {}  # Словарь для хранения экранов
        self.current_user_id = None  # Текущий пользователь

    def main(self, page: ft.Page):
        """
        Запускает основную логику приложения.
        """
        self.page = page
        self.page.title = "Streamlitify"  # Название приложения
        self.page.theme_mode = self.theme_mode  # Установка темы приложения
        self.page.window_width = 1200  # Ширина окна
        self.page.window_height = 850  # Высота окна
        self.page.window_center()  # Центрируем окно

        # Инициализация экранов приложения
        self.screens["main"] = MainScreen(page, self)
        self.screens["signin"] = SignInScreen(page, self)
        self.screens["register"] = RegisterScreen(page, self)
        self.screens["mainmenu"] = MainMenuScreen(page, self)
        self.screens["profile"] = ProfileScreen(page, self)
        self.screens["test1"] = TestScreen1(page, self)
        self.screens["theory1"] = TheoryScreen1(page, self)
        self.screens["simulator1"] = SimulatorScreen1(page, self)
        self.screens["testresults"] = TestResultsScreen(page, self)
        self.screens["simulatorresults"] = SimulatorResultsScreen(page, self)

        self.show_screen("main")  # Показать главный экран

    def show_screen(self, screen_name):
        """
        Переключает приложение на указанный экран.
        """
        self.page.clean()  # Очистка страницы перед показом нового экрана
        self.screens[screen_name].show()  # Показ нового экрана


# Запускаем приложение с помощью ft.app()
ft.app(target=StreamlitLearnApp().main, view=ft.FLET_APP)
