import flet as fl

section1 = fl.Container(
    bgcolor="#0896BA",
    padding=20,
    height=100,
    content=fl.Column(
        [
            fl.Row(
                [
                    fl.Container(
                        ink=True,
                        on_click=lambda e: print("Promosi"),
                        content=fl.Row(
                            [
                                fl.Icon(name="menu", color="white", size=20),
                                fl.Text("Promosi", size=15, color="white"),
                            ],
                            spacing=1,
                        ),
                    ),
                    fl.Container(
                        ink=True,
                        on_click=lambda e: print("Home"),
                        content=fl.Row(
                            [
                                fl.Icon(name="home", color="white", size=20),
                                fl.Text("Home", size=15, color="white"),
                            ],
                            spacing=1,
                        ),
                    ),
                    fl.Container(
                        ink=True,
                        on_click=lambda e: print("Chat"),
                        content=fl.Row(
                            [
                                fl.Icon(name="message", color="white", size=20),
                                fl.Text("Chat", size=15, color="white"),
                            ],
                            spacing=1,
                        ),
                    ),
                ],
                spacing=0,
                alignment="spaceEvenly",
            ),
        ],
        alignment="start",
    ),
)
