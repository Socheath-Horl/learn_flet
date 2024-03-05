import flet as ft

from app_bar import app_bar
from body import body_section


def main(page: ft.Page):
    page.bgcolor = "lightblue"
    page.scroll = True
    page.add(
        app_bar,
        body_section(page),
    )


ft.app(main)
