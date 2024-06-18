import flet as ft


class BaseScreen:
    """
    Базовый класс для всех экранов приложения.
    """

    def __init__(self, page, app):
        """
        Инициализирует базовый экран.
        """
        self.page = page  # Экземпляр страницы Flet
        self.app = app  # Экземпляр приложения
        # Кнопка для переключения темы (светлая/темная)
        self.theme_button = ft.IconButton(
            icon=ft.icons.BRIGHTNESS_6,  # Иконка переключателя темы
            on_click=self.switch_theme,  # Метод, вызываемый при нажатии кнопки
            icon_color=ft.colors.PURPLE,  # Цвет иконки
        )

    def switch_theme(self, e):
        """
        Переключает тему приложения между светлой и темной.
        """
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.update()  # Обновляет страницу после смены темы

    def build(self):
        """
        Метод для построения интерфейса, должен быть переопределен в наследуемых классах.
        """
        pass

    def show(self):
        """
        Добавляет интерфейс на страницу.
        """
        self.page.add(self.build())  # Добавляем интерфейс на страницу
