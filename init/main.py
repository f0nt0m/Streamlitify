import flet as ft
from init.mainscreen import MainScreen
from init.signin import SignInScreen
from init.register import RegisterScreen
from init.mainmenu import MainMenuScreen
from init.profile import ProfileScreen
from screens.test1 import TestScreen1
from screens.theory1 import TheoryScreen1
from screens.theory2 import TheoryScreen2
from screens.theory3 import TheoryScreen3
from screens.theory4 import TheoryScreen4
from screens.theory5 import TheoryScreen5
from screens.theory6 import TheoryScreen6
from screens.simulator1 import SimulatorScreen1
from screens.testresults import TestResultsScreen

class StreamlitLearnApp:
    def __init__(self):
        self.page = None
        self.theme_mode = ft.ThemeMode.SYSTEM
        self.login = None
        self.email = None
        self.screens = {}
        self.current_user_id = None  # Текущий пользователь

    def main(self, page: ft.Page):
        self.page = page
        self.page.title = "Streamlitify"
        self.page.theme_mode = self.theme_mode
        self.page.window_width = 1200
        self.page.window_height = 850
        self.page.window_center()

        self.screens["main"] = MainScreen(page, self)
        self.screens["signin"] = SignInScreen(page, self)
        self.screens["register"] = RegisterScreen(page, self)
        self.screens["mainmenu"] = MainMenuScreen(page, self)
        self.screens["profile"] = ProfileScreen(page, self)
        self.screens["test1"] = TestScreen1(page, self)
        self.screens["theory1"] = TheoryScreen1(page, self)
        self.screens["theory2"] = TheoryScreen2(page, self)
        self.screens["theory3"] = TheoryScreen3(page, self)
        self.screens["theory4"] = TheoryScreen4(page, self)
        self.screens["theory5"] = TheoryScreen5(page, self)
        self.screens["theory6"] = TheoryScreen6(page, self)
        self.screens["simulator1"] = SimulatorScreen1(page, self)
        self.screens["testresults"] = TestResultsScreen(page, self)

        self.show_screen("main")

    def show_screen(self, screen_name):
        self.page.clean()
        self.screens[screen_name].show()

# Запускаем приложение с помощью ft.app()
ft.app(target=StreamlitLearnApp().main, view=ft.FLET_APP)
