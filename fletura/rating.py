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
                    # TextButton(icon=icons.ABC_OUTLINED),
                    scale=2.0,
                    padding=padding.all(0),
                )
            )
            for _ in range(self.max_value)
        ]
        self.spacing = 4
        self.alignment = "center"

    def on_icon_clicked(self, e):
        rating_list = e.control.parent.parent.controls
        index = rating_list.index(e.control.parent)
        # print(index)
        # if index >= 0:
        for i in range(0, index + 1):
            print(i)
            rating_list[i].content.selected = True if e.control.data == True else False
            rating_list[i].content.data = not e.control.selected
            # e.control.selected = True if e.control.data == True else False
            # e.control.data = not e.control.selected
            rating_list[i].update()
        # elif


def main(page: Page):
    page.vertical_alignment = "center"
    page.alignment = "center"
    page.add(
        Rating(),
        # Container(Icon(icons.ZOOM_IN_MAP_ROUNDED), on_click=lambda _: print("clicked")),
    )


if __name__ == "__main__":
    app(target=main)
