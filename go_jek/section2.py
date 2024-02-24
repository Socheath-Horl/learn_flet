import flet as fl

section2 = fl.ResponsiveRow(
    [
        fl.Container(
            bgcolor="#FFFFFF",
            border_radius=fl.border_radius.only(top_left=30, top_right=30),
            padding=0,
            margin=fl.margin.symmetric(vertical=-30),
            content=fl.Column(
                col={"sm": 12, "md": 12, "lg": 12},
                controls=[
                    # Search box
                    fl.Container(
                        bgcolor="#FCFCFC",
                        border_radius=30,
                        content=fl.Row(
                            [
                                fl.TextField(
                                    border="none",
                                    prefix_icon=fl.icons.SEARCH,
                                    label="Search Lunch?",
                                ),
                                fl.IconButton(
                                    icon=fl.icons.ACCOUNT_CIRCLE,
                                    icon_color="green",
                                    icon_size=30,
                                ),
                            ],
                            alignment="spaceEvenly",
                        ),
                    ),
                    # Blue Card
                    fl.Card(
                        elevation=30,
                        content=fl.Container(
                            border_radius=10,
                            bgcolor="#01ADD5",
                            content=fl.Row(
                                [
                                    fl.Container(
                                        margin=10,
                                        height=70,
                                        padding=10,
                                        width=120,
                                        border_radius=10,
                                        bgcolor="white",
                                        content=fl.Column(
                                            [
                                                fl.Text(
                                                    "Gopay",
                                                    weight="bold",
                                                    size=15,
                                                ),
                                                fl.Text(
                                                    "USD 10.50",
                                                    weight="bold",
                                                    size=17,
                                                ),
                                                fl.Text(
                                                    "Tap to Topup",
                                                    size=11,
                                                ),
                                            ],
                                            alignment="center",
                                            spacing=0,
                                        ),
                                    ),
                                    # child icon
                                    fl.Column(
                                        [
                                            fl.Icon(
                                                name="bolt",
                                                color="white",
                                                size=30,
                                            ),
                                            fl.Text(
                                                "Pay",
                                                color="white",
                                                size=15,
                                                weight="bold",
                                            ),
                                        ],
                                        alignment="center",
                                        horizontal_alignment="center",
                                    ),
                                    fl.Column(
                                        [
                                            fl.Icon(
                                                name="add_box",
                                                color="white",
                                                size=30,
                                            ),
                                            fl.Text(
                                                "Topup",
                                                color="white",
                                                size=15,
                                                weight="bold",
                                            ),
                                        ],
                                        alignment="center",
                                        horizontal_alignment="center",
                                    ),
                                    fl.Column(
                                        [
                                            fl.Icon(
                                                name="drag_indicator",
                                                color="white",
                                                size=30,
                                            ),
                                            fl.Text(
                                                "More",
                                                color="white",
                                                size=15,
                                                weight="bold",
                                            ),
                                        ],
                                        alignment="center",
                                        horizontal_alignment="center",
                                    ),
                                ],
                                alignment="spaceEvenly",
                            ),
                        ),
                    ),
                ],
            ),
        )
    ]
)
