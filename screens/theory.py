import flet as ft
from init.basescreen import BaseScreen


class TheoryScreen(BaseScreen):

    def __init__(self, page, app):
        super().__init__(page, app)
        self.theory_title = ft.Text("", size=30, weight=ft.FontWeight.BOLD)
        self.theory_text = ft.Column(width=600)
        self.next_topic_button = ft.ElevatedButton(
            text="",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=200,
        )
        self.go_back_button = ft.TextButton(
            text="",
            on_click=self.go_back,
            style=ft.ButtonStyle(color=ft.colors.PURPLE),
        )
        self.logo_text = ft.Text(
            "Streamlitify",
            size=25,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.PURPLE,
        )

    def go_back(self, e):
        self.app.show_screen("mainmenu")

    def copy_to_clipboard(self, e, text):
        self.page.set_clipboard(text)
        self.page.snack_bar = ft.SnackBar(ft.Text("Copied to clipboard!"))
        self.page.snack_bar.open = True
        self.page.update()

    def update_texts(self):
        self.theory_title.value = self.app.translations[self.app.language][
            "theory"
        ]

        theory_paragraphs = [
            "Introduction to Streamlit\n\n",
            "Streamlit is an open-source app framework for Machine Learning and Data Science projects. "
            "It allows you to create beautiful, custom web apps for machine learning and data science with minimal effort.\n\n"
            "Key Features:\n\n"
            "Easy to Use: Streamlit’s simple API allows you to build interactive applications with just a few lines of Python code.\n"
            "Interactive Widgets: Streamlit offers a variety of widgets that make it easy to add interactivity to your apps.\n"
            "Real-Time Updates: Streamlit automatically updates your app in real-time as you modify your code, enabling a seamless development experience.\n"
            "Visualization: It supports all the major visualization libraries such as Matplotlib, Plotly, and Altair, making it easy to create dynamic visualizations.\n"
            "Deployment: Streamlit apps can be easily shared and deployed using Streamlit Cloud or other hosting services.\n\n",
            "Getting Started:\n\n",
            "Installation: You can install Streamlit using pip: ",
            'Creating Your First App: Start with a simple "Hello, World!" app. Create a new Python file and add:\n',
            "Running the App: Run your app using the command: ",
            "Streamlit helps you turn data scripts into shareable web apps in minutes, making it an invaluable tool for data scientists and machine learning engineers.",
        ]

        code_snippets = [
            "pip install streamlit",
            "import streamlit as st\n\n"
            'st.title("Hello, Streamlit!")\n'
            'st.write("This is your first Streamlit app.")',
            "streamlit run your_script.py",
        ]

        self.theory_text.controls.clear()

        for i, paragraph in enumerate(theory_paragraphs):
            self.theory_text.controls.append(ft.Text(paragraph, size=16))
            if i in [6, 8, 10]:
                self.theory_text.controls.append(
                    self.create_code_block(code_snippets.pop(0))
                )

        self.next_topic_button.text = self.app.translations[self.app.language][
            "next_topic"
        ]
        self.go_back_button.text = self.app.translations[self.app.language][
            "return_to_main_menu"
        ]
        self.language_selector.value = self.app.language
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
                        on_click=lambda e: self.copy_to_clipboard(
                            e, code_text
                        ),
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

    def build(self):
        theory_container = ft.Container(
            content=ft.Column(
                [
                    self.theory_title,
                    ft.Column(
                        [
                            ft.Container(
                                content=self.theory_text,
                                height=400,
                                expand=True,
                            )
                        ],
                        scroll=ft.ScrollMode.AUTO,
                        expand=True,
                    ),
                    self.next_topic_button,
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=10,
            border=ft.border.all(color=ft.colors.PURPLE, width=2),
            padding=20,
            expand=True,
            width=750,
            height=600,
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
                    content=theory_container,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Row(
                    [
                        self.language_selector,
                        ft.Container(expand=True),
                        self.theme_button,
                    ]
                ),
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        return theory_page_container
