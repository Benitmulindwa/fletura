from flet import *
from dataclasses import dataclass
import re


@dataclass
class RatingSize:
    small = 0.7
    medium = 1
    large = 1.5
    extralarge = 2


@dataclass
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
        rating_icon: str = icons.STAR_OUTLINE_OUTLINED,
        size: str = "large",
        color: str = colors.WHITE,
        selection_color: str = colors.ORANGE,
        selection_icon: str = None,
        on_hover_color: str = colors.ORANGE,
    ):
        super().__init__()

        self.max_value: int = max_value
        self.rating_value: float = rating_value
        self.rating_icon: str = rating_icon
        self.selection_icon: str = selection_icon
        self.size = size
        self.selection_color: str = selection_color
        self.color: str = color
        self.on_hover_color: str = on_hover_color
        self.rating_type: str = rating_type

        self.controls = [
            Container(
                IconButton(
                    icon=self.rating_icon,
                    icon_color=self.color,
                    selected_icon_color=self.selection_color,
                    selected_icon=self.selection_icon,
                    data=True,
                    on_click=(
                        self.on_icon_clicked
                        if self.rating_type == RatingType.CONTROLLED
                        else None
                    ),
                    style=ButtonStyle(
                        color={
                            MaterialState.HOVERED: (
                                self.on_hover_color
                                if self.rating_type == RatingType.CONTROLLED
                                else None
                            ),
                        },
                        overlay_color={
                            MaterialState.HOVERED: colors.TRANSPARENT,
                            MaterialState.FOCUSED: colors.WHITE,
                        },
                        padding=padding.all(0),
                    ),
                    scale=1.0,
                    mouse_cursor=(
                        MouseCursor.CLICK
                        if self.rating_type == RatingType.CONTROLLED
                        else MouseCursor.ALIAS
                    ),
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
        self.opacity = 0.4 if self.rating_type == RatingType.DISABLED else 1

        # implement
        if self.rating_value != 0 and (
            self.rating_type == RatingType.READONLY
            or self.rating_type == RatingType.DISABLED
        ):
            if str(self.rating_value).isdigit() == False:
                for i in range(int(self.rating_value) + 1):
                    self.controls[i].content.selected = True
                    if str(self.rating_value).isdigit() == False:

                        self.controls[
                            (int(self.rating_value))
                        ].content.selected_icon = "STAR_HALF"
            else:
                for i in range(int(self.rating_value)):
                    self.controls[i].content.selected = True

    def icon_hovered(self, e):
        # e.control.content.selected = True if e.data == "true" else False
        e.control.content.scale = 1.5 if e.data == "true" else 1.0
        e.control.content.icon_color = (
            self.on_hover_color if e.data == "true" else self.color
        )
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
        Rating(
            rating_icon=icons.STAR_OUTLINE_OUTLINED,
            selection_icon=icons.STAR,
            max_value=5,
            rating_type=RatingType.CONTROLLED,
            # on_hover_color="white",
        ),
        Rating(
            max_value=5,
            selection_icon=icons.STAR,
            rating_value=2.5,
            rating_type=RatingType.READONLY,
        ),
        Rating(
            rating_icon=cupertino_icons.HEART,
            selection_icon=cupertino_icons.HEART_FILL,
            max_value=5,
            rating_value=2.5,
            rating_type=RatingType.DISABLED,
        ),
    )


if __name__ == "__main__":
    app(target=main)
