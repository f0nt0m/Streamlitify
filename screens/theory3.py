import flet as ft
from init.basescreen import BaseScreen

class TheoryScreen3(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.theory_title = ft.Text("Theory - Advanced Topics", size=30, weight=ft.FontWeight.BOLD)
        self.theory_text = ft.Column(width=600, spacing=0)
        self.next_topic_button = ft.ElevatedButton(
            text="Finish",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=200,
        )
        self.go_back_button = ft.TextButton(
            text="Return to main menu",
            on_click=self.go_back,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
        )
        self.logo_text = ft.Text(
            "Streamlitify",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )
        self.scroll_container = None

    def go_back(self, e):
        self.app.show_screen("mainmenu")

    def copy_to_clipboard(self, e, text):
        self.page.set_clipboard(text)
        self.page.snack_bar = ft.SnackBar(ft.Text("Copied to clipboard!"))
        self.page.snack_bar.open = True
        self.page.update()

    def create_code_block(self, code_text):
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
            margin=ft.margin.symmetric(vertical=5),  # Добавлен вертикальный отступ между блоками
        )

    def build(self):
        content = [
            ft.Text("Advanced Streamlit Features\n", size=16),
            ft.Text("In this section, we'll cover some of the more advanced features of Streamlit.\n", size=16),
            ft.Text("Caching\n", size=16),
            ft.Text("Streamlit's caching mechanism allows you to store expensive computations so that they don't need to be re-run every time your script is executed. Use the @st.cache decorator to cache a function's output:\n", size=16),
            self.create_code_block(
                "import streamlit as st\n"
                "import time\n\n"
                "@st.cache\n"
                "def expensive_computation(a, b):\n"
                "    time.sleep(2)\n"
                "    return a * b\n\n"
                "result = expensive_computation(2, 3)\n"
                'st.write("Result:", result)'
            ),
            ft.Text("\nCustom Components\n", size=16),
            ft.Text("You can create your own custom components in Streamlit using the streamlit.components.v1 module. This allows you to embed custom HTML, CSS, and JavaScript code directly into your Streamlit apps:\n", size=16),
            self.create_code_block(
                "import streamlit as st\n"
                "import streamlit.components.v1 as components\n\n"
                "# Define your custom component\n"
                "def custom_component(html_code):\n"
                "    components.html(html_code)\n\n"
                "# Use the custom component in your app\n"
                'custom_component("<h1 style=\'color:red;\'>Hello, World!</h1>")'
            ),
            ft.Text("\nSession State\n", size=16),
            ft.Text("Streamlit provides a way to persist data across different runs of your script with session state. This can be useful for keeping track of user input or other stateful information:\n", size=16),
            self.create_code_block(
                "import streamlit as st\n\n"
                "# Initialize state\n"
                "if 'counter' not in st.session_state:\n"
                "    st.session_state.counter = 0\n\n"
                "# Increment counter\n"
                "if st.button('Increment'):\n"
                "    st.session_state.counter += 1\n\n"
                'st.write("Counter value:", st.session_state.counter)'
            ),
            ft.Text("\nThese advanced features can help you build more powerful and interactive Streamlit applications.", size=16),
        ]

        self.theory_text.controls.clear()
        self.theory_text.controls.extend(content)

        self.scroll_container = ft.Container(
            content=ft.Column(
                [
                    self.theory_title,
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=self.theory_text,
                                    height=400,  # Фиксированная высота для текста
                                    expand=True,
                                )
                            ],
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,  # Включили автоматический скроллинг
                        ),
                        height=400,  # Фиксированная высота для контейнера с текстом
                        expand=True,
                    ),
                    self.next_topic_button,
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
                        self.logo_text,
                        ft.Container(expand=True),
                        self.go_back_button,
                    ]
                ),
                ft.Container(
                    content=self.scroll_container,
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
        return theory_page_container
