import flet as ft
import asyncio
from screens.mainscreen import MainScreen
from screens.signin import SignInScreen
from screens.register import RegisterScreen
from screens.mainmenu import MainMenuScreen
from screens.test import TestScreen
from screens.theory import TheoryScreen
from screens.simulator import SimulatorScreen


class StreamlitLearnApp:
    def __init__(self):
        self.page = None
        self.language = "en"  # default language
        self.theme_mode = ft.ThemeMode.LIGHT  # default theme mode
        self.username = "username"
        self.translations = {
            "en": {
                "welcome": "Welcome to",
                "app_name": "Streamlitify",
                "subtitle": "Unlock the power of data with Streamlitify",
                "start": "Start Learning",
                "exit": "Exit",
                "contact": "Contact me",
                "support": "Support me",
                "signin": "Sign in",
                "email": "Email or login",
                "password": "Password",
                "register": "Register",
                "go_back": "Go back",
                "nickname": "Nickname",
                "register_link": "Register",
                "signin_link": "New to Streamlitify? Register",
                "main_menu": "Menu",
                "main_menu_select": "Select from the list below:",
                "theory": "Theory",
                "test": "Test",
                "simulator": "Simulator",
                "signout": "Sign out",
                "signed_in_as": "You have signed in as ",
                "options": "Options:",
                "primary_purpose_question": "What is the primary purpose of the Streamlit framework?",
                "primary_purpose_option1": "To build web applications for data science and machine learning",
                "primary_purpose_option2": "To create static websites with HTML and CSS",
                "primary_purpose_option3": "To manage databases and perform SQL queries",
                "next_question": "To the next question",
                "return_to_main_menu": "Return to main menu",
                "choose_right_answer": "Choose the right answer",
                "next_topic": "To the next topic",
            },
            "ru": {
                "welcome": "Добро пожаловать в",
                "app_name": "Streamlitify",
                "subtitle": "Раскройте силу данных с Streamlitify",
                "start": "Начать обучение",
                "exit": "Выход",
                "contact": "Связаться со мной",
                "support": "Поддержите меня",
                "signin": "Войти",
                "email": "Эл. адрес или логин",
                "password": "Пароль",
                "register": "Регистрация",
                "go_back": "Назад",
                "nickname": "Никнейм",
                "register_link": "Регистрация",
                "signin_link": "Впервые в Streamlitify? Регистрация",
                "main_menu": "Меню",
                "main_menu_select": "Выберите из списка ниже:",
                "theory": "Теория",
                "test": "Тест",
                "simulator": "Симулятор",
                "signout": "Выйти",
                "signed_in_as": "Вы вошли как ",
                "options": "Варианты ответа:",
                "primary_purpose_question": "Какова основная цель фреймворка Streamlit?",
                "primary_purpose_option1": "Для создания веб-приложений для обработки данных и машинного обучения",
                "primary_purpose_option2": "Для создания статических веб-сайтов с помощью HTML и CSS",
                "primary_purpose_option3": "Для управления базами данных и выполнения SQL-запросов",
                "next_question": "К следующему вопросу",
                "return_to_main_menu": "Вернуться в главное меню",
                "choose_right_answer": "Выберите правильный ответ",
                "next_topic": "К следующей теме",
            },
        }
        self.screens = {}

    def main(self, page: ft.Page):
        self.page = page
        self.page.title = "Streamlitify"
        self.page.theme_mode = self.theme_mode  # начальная тема
        self.page.window_width = 1200
        self.page.window_height = 850
        self.page.window_center()

        self.screens["main"] = MainScreen(page, self)
        self.screens["signin"] = SignInScreen(page, self)
        self.screens["register"] = RegisterScreen(page, self)
        self.screens["mainmenu"] = MainMenuScreen(page, self)
        self.screens["test"] = TestScreen(page, self)
        self.screens["theory"] = TheoryScreen(page, self)
        self.screens["simulator"] = SimulatorScreen(page, self)

        self.show_screen("main")

    def show_screen(self, screen_name):
        self.page.clean()
        self.screens[screen_name].show()
        self.screens[screen_name].update_texts()


async def run_app():
    app_instance = StreamlitLearnApp()
    await ft.app_async(target=app_instance.main, view=ft.FLET_APP)


if __name__ == "__main__":
    asyncio.run(run_app())
