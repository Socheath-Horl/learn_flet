import flet as ft
from urllib.parse import urlparse


def main(page: ft.Page):
    def view_pop(view):
        page.views.pop()
        my_view = page.views[-1]
        page.go(my_view.route)

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        title=ft.Text(
                            "Home Page",
                            size=30,
                            color="white",
                        ),
                        bgcolor="red500",
                    ),
                    ft.Text(page.route),
                    ft.ElevatedButton(
                        "Goto Second Page",
                        on_click=lambda _: page.go(f"/second/{your_params}"),
                    ),
                ],
            )
        )

        # Get param from home page
        param = page.route

        # get value after second page
        res = urlparse(param).path.split("/")[-1]
        print(f"Test Res is: {res}")
        if page.route == f"/second/{res}":
            page.views.append(
                ft.View(
                    f"/second/{res}",
                    [
                        ft.AppBar(
                            title=ft.Text(
                                "Second Page",
                                color="white",
                                size=30,
                            ),
                            bgcolor="blue500",
                        ),
                        ft.Text(page.route),
                        ft.Text(f"Your params is {res}"),
                        ft.ElevatedButton(
                            "Back to Home Page",
                            on_click=lambda _: page.go("/"),
                        ),
                    ],
                )
            )

    page.title = "Routing Apps"
    your_params = "watermelon"

    page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    p = ft.TemplateRoute(page.route)
    if p.match("/second/:id"):
        print("You're here", p.id)
    else:
        print("Whatever")


ft.app(main, view=ft.WEB_BROWSER)
