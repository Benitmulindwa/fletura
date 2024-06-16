from flet import *
from dataclasses import dataclass


@dataclass
class RatingSize:
    small = 0.5
    medium = 1
    large = 2


class Rating(Row):
    def __init__(
        self, max_value: int = 5, rating_value: float = 0.0, rating_icon: str = None
    ):
        super().__init__()

        self.max_value: int = max_value
        self.rating_value: float = rating_value
        self.rating_icon: str = rating_icon

        self.controls = [
            Container(
                IconButton(
                    icon=icons.STAR_OUTLINE_OUTLINED,
                    selected_icon_color="yellow",
                    selected_icon=icons.STAR,
                    data=True,
                    on_click=self.on_icon_clicked,
                    content=Icon(icons.ACCOUNT_TREE),
                    style=ButtonStyle(
                        overlay_color={
                            MaterialState.HOVERED: colors.TRANSPARENT,
                            MaterialState.FOCUSED: colors.BLUE,
                            MaterialState.DEFAULT: colors.WHITE,
                        },
                    ),
                    scale=1.0,
                    padding=padding.all(0),
                )
            )
            for _ in range(self.max_value)
        ]
        self.spacing = 0
        self.alignment = "center"

    def on_icon_clicked(self, e):
        rating_list = e.control.parent.parent.controls
        index = rating_list.index(e.control.parent)
        # print(index)
        # if index >= 0:
        for i in range(0, index + 2):
            # print(i)
            rating_list[i].content.selected = True
            rating_list[i].content.data = not rating_list[i].content.selected

            rating_list[i].update()

        for i in range(index, len(rating_list)):

            rating_list[i].content.selected = False
            rating_list[i].content.data = not rating_list[i].content.selected
            rating_list[i].update()


def main(page: Page):
    page.vertical_alignment = "center"
    page.alignment = "center"
    page.add(
        Rating(max_value=10),
    )


if __name__ == "__main__":
    app(target=main)
