import flet as ft
from init.basescreen import BaseScreen


class MainScreen(BaseScreen):
    """
    Экран приветствия и начала обучения.
    """

    def __init__(self, page, app):
        """
        Инициализирует главный экран.
        """
        super().__init__(page, app)
        self.welcome_text = ft.Text(
            "Welcome to", size=40, text_align=ft.TextAlign.CENTER
        )
        self.app_name_text = ft.Text(
            "Streamlitify",
            size=60,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )
        self.subtitle_text = ft.Text(
            "Unlock the power of data with Streamlitify",
            size=25,
            text_align=ft.TextAlign.CENTER,
        )
        self.start_button = ft.ElevatedButton(
            text="Start Learning",
            on_click=self.start_clicked,  # Метод, вызываемый при нажатии кнопки начала
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=200,
            height=50,
        )
        self.exit_button = ft.TextButton(
            text="Exit",
            on_click=self.confirm_exit,  # Метод, вызываемый при нажатии кнопки выхода
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            height=40,
        )
        self.contact_button = ft.TextButton(
            text="Contact me",
            on_click=lambda e: page.launch_url("https://t.me/f0ntt0m"),  # Открытие ссылки при нажатии
            icon=ft.icons.SEND,
            icon_color=ft.colors.PURPLE,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            height=40,
        )
        self.support_button = ft.TextButton(
            text="Support me",
            on_click=lambda e: page.launch_url(
                "https://www.tinkoff.ru/cf/188uzPH7nwb"
            ),  # Открытие ссылки при нажатии
            icon=ft.icons.SEARCH,
            icon_color=ft.colors.PURPLE,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            height=40,
        )
        self.github_button = ft.TextButton(
            text="GitHub",
            on_click=lambda e: page.launch_url("https://github.com/f0nt0m"),  # Открытие ссылки при нажатии
            icon=ft.icons.CODE,
            icon_color=ft.colors.PURPLE,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
            height=40,
        )

    def start_clicked(self, e):
        """
        Переключает приложение на экран входа.
        """
        self.app.show_screen("signin")  # Показ экрана входа

    def confirm_exit(self, e):
        """
        Подтверждает выход из приложения.
        """

        def on_confirm(result):
            if result == "yes":
                self.app.page.window_close()  # Закрываем окно приложения
            else:
                dialog.open = False
                self.app.page.update()

        dialog = ft.AlertDialog(
            title=ft.Text("Confirm Exit", color=ft.colors.PURPLE),
            content=ft.Text("Are you sure you want to exit?", color=ft.colors.PURPLE),
            actions=[
                ft.TextButton("Yes", on_click=lambda e: on_confirm("yes"), style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.PURPLE)),
                ft.TextButton("No", on_click=lambda e: on_confirm("no"), style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.PURPLE)),
            ],
            bgcolor=ft.colors.WHITE,
        )
        self.app.page.dialog = dialog
        dialog.open = True
        self.app.page.update()

    def build(self):
        """
        Строит и возвращает интерфейс главного экрана.
        """
        main_container = ft.Column(
            [
                self.welcome_text,
                self.app_name_text,
                self.subtitle_text,
                ft.Container(height=20),
                self.start_button,
                self.exit_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        footer_container = ft.Row(
            [
                self.contact_button,
                ft.Container(expand=True),
                self.support_button,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.END,
        )

        centered_container = ft.Container(
            content=main_container,
            alignment=ft.alignment.center,
            expand=True,
        )

        # Перемещаем github_button сюда
        full_container = ft.Column(
            [
                ft.Row(
                    [
                        self.github_button,  # Кнопка GitHub в левом верхнем углу
                        ft.Container(expand=True),
                        self.theme_button,
                    ]
                ),
                centered_container,
                footer_container,
            ],
            expand=True,
        )

        return full_container
