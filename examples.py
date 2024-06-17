from flet import *
from fletura import Paper, Rating, RatingType


def main(page: Page):
    page.add(
        Paper(
            bgcolor="#ffffff",
            width=200,
            height=50,
        ),
        Rating(
            max_value=5, selection_icon=icons.STAR, rating_type=RatingType.CONTROLLED
        ),
        Rating(
            max_value=5,
            # selection_icon=icons.STAR,
            rating_value=2.5,
            rating_type="readonly",
            size="large",
        ),
    )


app(target=main)
