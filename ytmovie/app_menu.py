import flet as fl

app_menu = fl.AppBar(
    bgcolor="black",
    center_title=True,
    leading=fl.IconButton(
        icon=fl.icons.MENU,
        icon_color="white",
        icon_size=30,
    ),
    title=fl.Text(
        "Movie X",
        size=30,
        color="white",
        weight="bold",
    ),
    actions=[
        fl.IconButton(
            icon=fl.icons.SEARCH,
            icon_color="white",
            icon_size=30,
        )
    ],
)
