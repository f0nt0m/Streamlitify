import flet as ft


class BaseScreen:
    def __init__(self, page, app):
        self.page = page
        self.app = app
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

    def build(self):
        pass

    def show(self):
        self.page.add(self.build())