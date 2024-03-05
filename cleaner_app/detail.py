import flet as fl


def detail_section(page: fl.Page):
    return fl.Column(
        [
            fl.Container(
                padding=20,
                margin=fl.margin.symmetric(vertical=30),
                bgcolor="black",
                border_radius=fl.border_radius.only(top_right=30, bottom_right=30),
                content=fl.Text(
                    "Can be deleted",
                    size=20,
                    weight="bold",
                    color="white",
                ),
            ),
            fl.Stack(
                [
                    fl.Card(
                        elevation=30,
                        content=fl.Container(
                            # width=page.window_width,
                            margin=fl.margin.only(top=-10),
                            height=300,
                            content=fl.Column(
                                [
                                    fl.ListTile(
                                        leading=fl.Icon(fl.icons.ADD_REACTION),
                                        title=fl.Text(
                                            "Junk Files",
                                            color="black",
                                            size=20,
                                            weight="bold",
                                        ),
                                        subtitle=fl.Row(
                                            [
                                                fl.Icon(
                                                    name="group_off",
                                                    color="red",
                                                    size=15,
                                                ),
                                                fl.Text(
                                                    "1.15 GB Found",
                                                    size=15,
                                                    color="grey",
                                                ),
                                            ]
                                        ),
                                    ),
                                    fl.ListTile(
                                        leading=fl.Icon(fl.icons.ADD_REACTION),
                                        title=fl.Text(
                                            "Trash Files",
                                            color="red",
                                            size=20,
                                            weight="bold",
                                        ),
                                        trailing=fl.ElevatedButton(
                                            "Let Cleaned",
                                            icon=fl.icons.WHATSHOT,
                                            color="green",
                                            icon_color="green",
                                        ),
                                        subtitle=fl.Row(
                                            [
                                                fl.Icon(
                                                    name="group_off",
                                                    color="red",
                                                    size=15,
                                                ),
                                                fl.Text(
                                                    "1.15 GB Found",
                                                    size=15,
                                                    color="grey",
                                                ),
                                            ]
                                        ),
                                    ),
                                    fl.ListTile(
                                        leading=fl.Icon(fl.icons.ADD_REACTION),
                                        title=fl.Text(
                                            "Slow Performance",
                                            color="orange",
                                            size=20,
                                            weight="bold",
                                        ),
                                        subtitle=fl.Row(
                                            [
                                                fl.Icon(
                                                    name="group_off",
                                                    color="red",
                                                    size=15,
                                                ),
                                                fl.Text(
                                                    "1.15 GB Found",
                                                    size=15,
                                                    color="grey",
                                                ),
                                            ]
                                        ),
                                    ),
                                ]
                            ),
                        ),
                    ),
                    fl.Row(
                        [
                            fl.Card(
                                elevation=20,
                                content=fl.Container(
                                    margin=fl.margin.symmetric(vertical=-30),
                                    padding=10,
                                    bgcolor="green",
                                    content=fl.Row(
                                        [
                                            fl.Icon(
                                                fl.icons.FAVORITE,
                                                color=fl.colors.PINK,
                                            ),
                                            fl.Text(
                                                "Health System",
                                                size=20,
                                                weight="bold",
                                                color="white",
                                            ),
                                        ]
                                    ),
                                ),
                            )
                        ],
                        alignment="end",
                    ),
                ]
            ),
            fl.Row(
                [
                    fl.Container(
                        ink=True,
                        padding=10,
                        border_radius=fl.border_radius.all(30),
                        border=fl.border.all(5, color="white"),
                        on_click=lambda e: print("Hello Test"),
                        content=fl.Row(
                            [
                                fl.Icon(
                                    fl.icons.TOUCH_APP,
                                    size=30,
                                    color="white",
                                ),
                                fl.Text(
                                    "Optimize Now",
                                    color="white",
                                    size=30,
                                ),
                            ]
                        ),
                    )
                ],
                alignment="center",
            ),
        ]
    )
