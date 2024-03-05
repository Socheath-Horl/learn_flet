import flet as fl

from dashboard import dashboard
from detail import detail_section


def body_section(page: fl.Page):
    return fl.Column(
        [
            dashboard,
            detail_section(page),
        ],
        spacing=0,
    )
