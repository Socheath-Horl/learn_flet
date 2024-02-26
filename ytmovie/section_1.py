import flet as fl
import json

base_url = "https://image.tmdb.org/t/p/original"
all_movie = fl.Row(scroll=True)
s = []

# Read data from file
with open("ytmovie/data.json") as json_file:
    data = json.load(json_file)
    s = data["results"]

# add new widget
for x in s:
    all_movie.controls.append(
        fl.Card(
            elevation=30,
            content=fl.Container(
                width=160,
                height=330,
                padding=10,
                border=fl.border.symmetric(
                    vertical=fl.border.BorderSide(5, "orange"),
                ),
                bgcolor="white",
                content=fl.Column(
                    [
                        fl.Image(
                            src=base_url + x["poster_path"],
                            height=200,
                            border_radius=fl.border_radius.all(30),
                            fit="contain",
                        ),
                        fl.Text(
                            x["original_title"],
                            size=18,
                            weight="bold",
                            text_align="center",
                        ),
                    ],
                    alignment="spaceAround",
                    horizontal_alignment="center",
                ),
            ),
        )
    )

mysection_1 = fl.Column(
    [
        fl.Text("Trending", size=20, weight="bold"),
        all_movie,
    ]
)
