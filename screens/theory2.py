import flet as ft
from init.basescreen import BaseScreen


class TheoryScreen2(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.theory_title = ft.Text("Theory - Components and Features", size=30, weight=ft.FontWeight.BOLD)
        self.theory_text = ft.Column(width=600, spacing=0)
        self.next_topic_button = ft.ElevatedButton(
            text="To the next topic",
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
            ft.Text("Streamlit Components and Features\n", size=16),
            ft.Text("Streamlit provides a variety of components to build interactive and rich applications. "
                    "Below are some of the core components and their usage examples.\n", size=16),
            ft.Text("Displaying Text\n", size=16),
            self.create_code_block(
                "import streamlit as st\n\n"
                'st.title("Streamlit App")\n'
                'st.header("This is a header")\n'
                'st.subheader("This is a subheader")\n'
                'st.text("This is a simple text")'
            ),
            ft.Text("\nInteractive Widgets\n", size=16),
            ft.Text("Streamlit offers various widgets to interact with the user. Here are some examples:\n", size=16),
            self.create_code_block(
                "import streamlit as st\n\n"
                'if st.button("Click me"):\n'
                '    st.write("Button clicked!")\n\n'
                'name = st.text_input("Enter your name")\n'
                'st.write(f"Hello, {name}!")\n\n'
                'age = st.slider("Select your age", 0, 100)\n'
                'st.write(f"You are {age} years old")'
            ),
            ft.Text("\nDisplaying Data\n", size=16),
            self.create_code_block(
                "import streamlit as st\n"
                "import pandas as pd\n\n"
                "data = {\n"
                "    'Name': ['John', 'Anna', 'Peter'],\n"
                "    'Age': [28, 24, 35],\n"
                "    'City': ['New York', 'Paris', 'Berlin']\n"
                "}\n\n"
                "df = pd.DataFrame(data)\n\n"
                "st.write('DataFrame:')\n"
                "st.dataframe(df)\n\n"
                "st.write('Table:')\n"
                "st.table(df)"
            ),
            ft.Text("\nVisualizing Data\n", size=16),
            ft.Text("Streamlit supports various libraries for data visualization. Here are a few examples using Matplotlib and Plotly:\n", size=16),
            self.create_code_block(
                "import streamlit as st\n"
                "import matplotlib.pyplot as plt\n"
                "import numpy as np\n\n"
                "# Matplotlib example\n"
                "x = np.linspace(0, 10, 100)\n"
                "y = np.sin(x)\n\n"
                "fig, ax = plt.subplots()\n"
                "ax.plot(x, y)\n\n"
                "st.pyplot(fig)"
            ),
            ft.Container(height=10),  # Добавлен отступ между блоками
            self.create_code_block(
                "import streamlit as st\n"
                "import plotly.express as px\n\n"
                "# Plotly example\n"
                "df = px.data.iris()\n"
                "fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')\n\n"
                "st.plotly_chart(fig)"
            ),
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
