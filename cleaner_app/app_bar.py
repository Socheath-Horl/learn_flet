import flet as fl

app_bar = fl.AppBar(
    bgcolor="lightblue",
    leading=fl.IconButton(icon=fl.icons.ARROW_BACK_IOS),
    title=fl.Text(
        "App Cleaner",
        color="white",
        weight="bold",
    ),
    actions=[
        fl.IconButton(
            icon=fl.icons.YOUTUBE_SEARCHED_FOR,
            icon_color=fl.colors.BLACK,
            icon_size=30,
        ),
        fl.IconButton(
            icon=fl.icons.STAR_RATE,
            icon_color=fl.colors.BLACK,
            icon_size=30,
        ),
    ],
)
