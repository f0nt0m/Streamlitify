import flet as ft
import json
from init.basescreen import BaseScreen

class TheoryScreen1(BaseScreen):
    """
    Экран с теоретической информацией.
    """
    def __init__(self, page, app):
        """
        Инициализирует экран с теоретической информацией.
        """
        super().__init__(page, app)
        self.page = page
        self.app = app
        self.theory_data = self.load_all_theories()  # Загружает данные из JSON-файла
        self.current_topic = 1  # Индекс текущего раздела теории
        self.theory_title = ft.Text(size=30, weight=ft.FontWeight.BOLD)  # Заголовок раздела теории
        self.theory_text = ft.Column(width=600, spacing=0)  # Текст раздела теории
        self.next_topic_button = ft.ElevatedButton(
            text="To the next topic",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=200,
            on_click=self.go_to_next_topic  # Обработчик нажатия на кнопку "Next"
        )
        self.previous_topic_button = ft.ElevatedButton(
            text="Previous topic",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.GREY,
            width=200,
            on_click=self.go_to_previous_topic,  # Обработчик нажатия на кнопку "Previous"
            disabled=True  # Изначально кнопка "Previous" неактивна
        )
        self.go_back_button = ft.TextButton(
            text="Return to main menu",
            on_click=self.go_back,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
        )  # Кнопка возврата в главное меню
        self.logo_text = ft.Text(
            "Streamlitify",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )  # Логотип приложения
        self.load_theory_content()  # Загрузка первого раздела теории

    def go_back(self, e):
        """
        Возвращает пользователя в главное меню.
        """
        self.app.show_screen("mainmenu")  # Показывает главное меню

    def go_to_next_topic(self, e):
        """
        Переходит к следующему разделу теории.
        """
        if self.current_topic < len(self.theory_data):  # Если есть следующий раздел
            self.current_topic += 1
            self.load_theory_content()  # Загружает следующий раздел
            self.page.update()  # Обновляет страницу
            if self.current_topic == len(self.theory_data):  # Если это последний раздел
                self.next_topic_button.disabled = True
                self.page.snack_bar = ft.SnackBar(ft.Text("You have completed all theory topics."))
                self.page.snack_bar.open = True
                self.page.update()

    def go_to_previous_topic(self, e):
        """
        Переходит к предыдущему разделу теории.
        """
        if self.current_topic > 1:
            self.current_topic -= 1
            self.load_theory_content()
            self.page.update()
        if self.current_topic < len(self.theory_data):
            self.next_topic_button.disabled = False

    def copy_to_clipboard(self, e, text):
        """
        Копирует текст в буфер обмена.
        """
        self.page.set_clipboard(text)
        self.page.snack_bar = ft.SnackBar(ft.Text("Copied to clipboard!"))
        self.page.snack_bar.open = True
        self.page.update()

    def create_code_block(self, code_text):
        """
        Создает элемент для отображения блока кода с кнопкой копирования.
        """
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Text(
                            code_text,
                            font_family="Courier",
                            size=16,
                            color=ft.colors.WHITE,
                        ),
                        expand=True,
                    ),
                    ft.IconButton(
                        icon=ft.icons.CONTENT_COPY,
                        on_click=lambda e: self.copy_to_clipboard(e, code_text),
                        tooltip="Copy to clipboard",
                        icon_color=ft.colors.WHITE,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=ft.colors.BLACK,
            padding=10,
            border_radius=5,
            margin=ft.margin.symmetric(vertical=5),
        )

    def load_all_theories(self):
        """
        Загружает все разделы теории из JSON-файла.
        """
        with open("text/theory.json", "r") as file:
            return json.load(file)

    def load_theory_content(self):
        """
        Загружает текст текущего раздела теории.
        """
        theory_key = f"theory{self.current_topic}"  # Формирует ключ для доступа к данным раздела теории
        theory_data = self.theory_data[theory_key]  # Получает данные раздела теории

        content = []
        self.theory_title.value = theory_data[0]  # Устанавливает заголовок раздела теории
        for item in theory_data[1:]:
            if item.startswith("CODE:"):
                content.append(self.create_code_block(item[5:]))  # Создает элемент блока кода
            else:
                content.append(ft.Text(item, size=16))  # Создает элемент обычного текста
            content.append(ft.Container(height=10))  # Добавляет отступ

        self.theory_text.controls.clear()  # Очищает предыдущее содержимое
        self.theory_text.controls.extend(content)  # Добавляет новое содержимое

        # Обновляет состояние кнопок "Previous" и "Next"
        self.update_buttons()

    def update_buttons(self):
        """
        Обновляет состояние кнопок "Previous" и "Next".
        """
        self.previous_topic_button.disabled = self.current_topic == 1  # Деактивирует "Previous", если это первый раздел
        self.previous_topic_button.bgcolor = ft.colors.GREY if self.current_topic == 1 else ft.colors.PURPLE  # Изменяет цвет "Previous"
        self.next_topic_button.disabled = self.current_topic == len(self.theory_data)  # Деактивирует "Next", если это последний раздел

    def build(self):
        """
        Строит и возвращает интерфейс экрана с теоретической информацией.
        """
        self.scroll_container = ft.Container(
            content=ft.Column(
                [
                    self.theory_title,  # Заголовок раздела теории
                    self.theory_text,  # Текст раздела теории
                    ft.Row(
                        [
                            self.previous_topic_button,  # Кнопка "Previous"
                            self.next_topic_button,  # Кнопка "Next"
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    )
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO
            ),
            border_radius=10,
            border=ft.border.all(color=ft.colors.PURPLE, width=2),
            padding=10,
            expand=True,
            width=750,
        )

        theory_page_container = ft.Column(
            [
                ft.Row(
                    [
                        self.logo_text,  # Логотип приложения
                        ft.Container(expand=True),  # Растягиваем пустой контейнер
                        self.go_back_button,  # Кнопка возврата в главное меню
                    ]
                ),
                ft.Container(
                    content=self.scroll_container,  # Элемент с текстом теории
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
        return theory_page_container