import flet as fl
import json

base_url = "https://image.tmdb.org/t/p/original"
all_movie = fl.Row(scroll=True)
s = []

# Read data from file
with open("ytmovie/comming.json") as json_file:
    data = json.load(json_file)
    s = data["results"]

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
                        fl.Text(
                            "Release Date: " + x["release_date"],
                            size=10,
                            color="red",
                            weight="bold",
                        ),
                    ],
                    alignment="spaceAround",
                    horizontal_alignment="center",
                ),
            ),
        )
    )

section_comming = fl.Container(
    bgcolor="black",
    border_radius=15,
    padding=15,
    content=fl.Column(
        [
            fl.Container(
                content=fl.Text(
                    "Comming soon",
                    size=20,
                    color="white",
                    weight="bold",
                )
            ),
            all_movie,
        ]
    ),
)
