from flet import *
from dataclasses import dataclass


@dataclass
class RatingSize:
    small = 0.7
    medium = 1
    large = 1.5
    extralarge = 2


class RatingType:
    CONTROLLED = "controlled"
    READONLY = "readonly"
    DISABLED = "disabled"


class Rating(Row):
    def __init__(
        self,
        rating_type: str = "controlled",
        max_value: int = 5,
        rating_value: float = 0.0,
        rating_icon: str = None,
        size: str = "large",
        color: str = colors.WHITE,
        selection_color: str = colors.YELLOW,
        on_hover_color: str = colors.YELLOW,
    ):
        super().__init__()

        self.max_value: int = max_value
        self.rating_value: float = rating_value
        self.rating_icon: str = rating_icon
        self.size = size
        self.selection_color: str = selection_color
        self.rating_type: str = rating_type

        self.controls = [
            Container(
                IconButton(
                    icon=icons.STAR_OUTLINE_OUTLINED,
                    selected_icon_color=self.selection_color,
                    selected_icon=icons.STAR,
                    data=True,
                    on_click=(
                        self.on_icon_clicked
                        if self.rating_type == RatingType.CONTROLLED
                        else None
                    ),
                    style=ButtonStyle(
                        color={
                            MaterialState.HOVERED: (
                                on_hover_color
                                if self.rating_type == RatingType.CONTROLLED
                                else None
                            ),
                        },
                        overlay_color={
                            MaterialState.HOVERED: colors.TRANSPARENT,
                            MaterialState.FOCUSED: colors.WHITE,
                            MaterialState.DEFAULT: color,
                        },
                        padding=padding.all(0),
                    ),
                    scale=1.0,
                    # padding=padding.all(0),
                ),
                margin=margin.all(-7),
                on_hover=(
                    self.icon_hovered
                    if self.rating_type == RatingType.CONTROLLED
                    else None
                ),
            )
            for _ in range(self.max_value)
        ]
        if size == "small":
            self.scale = RatingSize.small
        elif size == "medium":
            self.scale = RatingSize.medium
        elif size == "extralarge":
            self.scale = RatingSize.extralarge
        else:
            self.scale = RatingSize.large

        self.spacing = 0
        self.alignment = "center"
        self.opacity = 0.5 if self.rating_type == RatingType.DISABLED else 1

    def icon_hovered(self, e):
        # e.control.content.selected = True if e.data == "true" else False
        e.control.content.scale = 1.5 if e.data == "true" else 1.0
        e.control.content.update()

    def on_icon_clicked(self, e):
        rating_list = e.control.parent.parent.controls
        index = rating_list.index(e.control.parent)
        for i in range(len(rating_list)):
            rating_list[i].content.selected = i <= index
            rating_list[i].update()


def main(page: Page):
    page.vertical_alignment = "center"
    page.alignment = "center"
    page.add(
        # Rating(max_value=5, size="small"),
        Rating(max_value=5, rating_type=RatingType.CONTROLLED),
        Rating(max_value=5, rating_type=RatingType.READONLY),
        Rating(max_value=5, rating_type=RatingType.DISABLED),
    )


if __name__ == "__main__":
    app(target=main)
