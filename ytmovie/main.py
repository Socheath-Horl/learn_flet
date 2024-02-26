import flet as ft

import app_menu
import section_1
import section_comming


def main(page: ft.Page):
    page.scroll = True
    page.add(
        app_menu.app_menu,
        section_1.mysection_1,
        section_comming.section_comming,
    )


ft.app(main)
