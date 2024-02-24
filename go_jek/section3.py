import flet as fl

section3 = fl.Container(
    margin=fl.margin.only(top=40, left=10),
    content=fl.Column(
        [
            fl.Text(
                "Top Picks for You",
                size=30,
                weight="bold",
            ),
            fl.Row(
                [
                    fl.Container(
                        margin=fl.margin.only(top=10),
                        border_radius=30,
                        padding=10,
                        bgcolor="#41AE62",
                        ink=True,
                        on_click=lambda e: print("All"),
                        border=fl.border.all(2, "#E1E1E1"),
                        content=fl.Text("All", size=13, color="white"),
                    ),
                    fl.Container(
                        margin=fl.margin.only(top=10),
                        border_radius=30,
                        padding=10,
                        ink=True,
                        on_click=lambda e: print("Covid-19"),
                        border=fl.border.all(2, "#E1E1E1"),
                        content=fl.Text("Covid-19", size=13, color="black"),
                    ),
                    fl.Container(
                        margin=fl.margin.only(top=10),
                        border_radius=30,
                        padding=10,
                        ink=True,
                        on_click=lambda e: print("Donation"),
                        border=fl.border.all(2, "#E1E1E1"),
                        content=fl.Text("Donation", size=13, color="black"),
                    ),
                    fl.Container(
                        margin=fl.margin.only(top=10),
                        border_radius=30,
                        padding=10,
                        ink=True,
                        on_click=lambda e: print("Entertainment"),
                        border=fl.border.all(2, "#E1E1E1"),
                        content=fl.Text("Entertainment", size=13, color="black"),
                    ),
                ],
                alignment="spaceAround",
            ),
            # Card Section
            fl.Container(
                margin=fl.margin.only(bottom=40),
                content=fl.Row(
                    [
                        fl.Card(
                            elevation=30,
                            content=fl.Container(
                                bgcolor="white",
                                padding=10,
                                content=fl.Column(
                                    [
                                        fl.Image(
                                            src="https://lelogama.go-jek.com/post_featured_image/header-paylater-voucher-gofood-plus.jpg",
                                            fit="contain",
                                            width=300,
                                            height=220,
                                        ),
                                        fl.Container(
                                            width=300,
                                            content=fl.Column(
                                                [
                                                    fl.Text(
                                                        "Get Up 50K Cashback",
                                                        size=20,
                                                        weight="bold",
                                                    ),
                                                    fl.Text(
                                                        """Upgrade to Gopay plus now, enjoy cashback up to 50K if you transact with PayLater!""",
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
                        fl.Card(
                            elevation=30,
                            content=fl.Container(
                                bgcolor="white",
                                padding=10,
                                content=fl.Column(
                                    [
                                        fl.Image(
                                            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrQRcwzqT4WSP0rPx6F4Wbup-OVoaHjiYwEg&usqp=CAU",
                                            fit="contain",
                                            width=300,
                                            height=220,
                                        ),
                                        fl.Container(
                                            width=300,
                                            content=fl.Column(
                                                [
                                                    fl.Text(
                                                        "Get Up 50K Cashback",
                                                        size=20,
                                                        weight="bold",
                                                    ),
                                                    fl.Text(
                                                        """Upgrade to Gopay plus now, enjoy cashback up to 50K if you transact with PayLater!""",
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
                    ],
                    scroll="always",
                ),
            ),
        ]
    ),
)
