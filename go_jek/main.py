import flet as ft

import app_menu
import section1
import section2
import section3
import bottom_bar


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.scroll = "auto"
    page.update()
    page.add(
        app_menu.app_menu,
        section1.section1,
        section2.section2,
        section3.section3,
        bottom_bar.bottom_bar,
    )


ft.app(main)
