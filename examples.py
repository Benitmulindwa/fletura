from flet import *
from fletura import Paper, Rating, Badge


def main(page: Page):
    page.add(
        Paper(
            bgcolor="#ffffff",
            width=200,
            height=50,
        ),
        Rating(max_value=5, selection_icon=icons.STAR, rating_type="controlled"),
        Rating(
            max_value=5,
            # selection_icon=icons.STAR,
            rating_value=2.5,
            rating_type="readonly",
            size="large",
        ),
        Text("Badge Component"),
        Badge(position="top_left"),
        Badge(cupertino_icons.CART, position="center_left", count=105, max_value=99),
        Badge(count=15, badge_color="purple500", position="top_left", max_value=9),
    )


app(target=main)
