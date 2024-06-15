import flet as ft


class BaseScreen:
    def __init__(self, page, app):
        self.page = page
        self.app = app
        self.language_selector = ft.Dropdown(
            options=[
                ft.dropdown.Option(text="English", key="en"),
                ft.dropdown.Option(text="Русский", key="ru"),
            ],
            width=100,
            value=self.app.language,  # Установим значение по умолчанию
            on_change=self.change_language,
        )
        self.theme_button = ft.IconButton(
            icon=ft.icons.BRIGHTNESS_6,
            on_click=self.switch_theme,
            icon_color=ft.colors.PURPLE,
        )

    def switch_theme(self, e):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.update()

    def change_language(self, e):
        self.app.language = self.language_selector.value
        self.update_texts()

    def update_texts(self):
        pass

    def build(self):
        pass

    def show(self):
        self.page.add(self.build())
