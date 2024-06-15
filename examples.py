from flet import *
from fletura import Paper


def main(page: Page):
    page.add(
        Paper(
            bgcolor="#ffffff",
            width=200,
            height=50,
        )
    )


app(target=main)
