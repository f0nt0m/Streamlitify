import flet as ft
from init.basescreen import BaseScreen


class SimulatorScreen1(BaseScreen):
    def __init__(self, page, app):
        super().__init__(page, app)
        self.simulator_title = ft.Text("Simulator", size=30, weight=ft.FontWeight.BOLD)
        self.code_snippet = ft.Text(
            """import streamlit as st

st.title("My Streamlit App")
st.write("This is a sample Streamlit app.")""",
            size=16,
            font_family="monospace",
            width=600,
        )
        self.user_input = ft.TextField(
            label="Your Code",
            hint_text="Enter corrected code",
            width=600,
            multiline=True,
            height=100,
        )
        self.check_button = ft.ElevatedButton(
            text="Check",
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE,
            width=250,
            on_click=self.check_code,
        )
        self.result_text = ft.Text("", size=16)
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

    def go_back(self, e):
        self.app.show_screen("mainmenu")

    def check_code(self, e):
        # Здесь реализация проверки кода
        user_code = self.user_input.value
        if (
                user_code
                == 'import streamlit as st\n\nst.title("My Streamlit App")\n'
                   'st.write("This is a sample Streamlit app.")'
        ):
            self.result_text.value = "Correct! You fixed the code!"
        else:
            self.result_text.value = "Oops, try again!"
        self.page.update()

    def build(self):
        simulator_container = ft.Container(
            content=ft.Column(
                [
                    self.simulator_title,  # Title at the top
                    ft.Container(  # Wrap code snippet in a container for spacing
                        content=ft.Column(  # Use a Column for vertical content
                            [
                                self.code_snippet,
                                self.user_input,
                            ],
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=20,  # Add padding to the code snippet container
                        expand=True,
                    ),
                    self.check_button,
                    self.result_text,
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.START,  # Align elements from the start
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=10,
            border=ft.border.all(color=ft.colors.PURPLE, width=2),
            padding=20,
            expand=True,
            width=750,
            height=600,
        )

        simulator_page_container = ft.Column(
            [
                ft.Row(
                    [
                        self.logo_text,
                        ft.Container(expand=True),
                        self.go_back_button,
                    ]
                ),
                ft.Container(
                    content=simulator_container,
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
        return simulator_page_container
