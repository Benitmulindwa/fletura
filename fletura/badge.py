from flet import *


class Badge(Container):
    def __init__(
        self,
        badge_icon: str = icons.MAIL,
        icon_color: str = "white",
        badge_color: str = "red",
        count: int = 19,
        max_value: int = 9,
        position: str = "top_left",
    ):
        super().__init__()
        self.max_value = max_value
        self.badge_color = badge_color
        self.content = Stack(
            [
                Container(
                    Icon(badge_icon, color=icon_color, size=30),
                    height=50,
                    width=60,
                    margin=margin.only(left=-16, right=15),
                ),
                self.create_badge(count, position),
            ]
        )

        self.alignment = alignment.center

    def create_badge(self, count: int, position: str):
        display_count = f"{count}" if count <= self.max_value else f"{self.max_value}+"

        # Adjasting the top container size based on whether a single,2 or 3 digits number are given
        badge_width = 20  # default width for single-digit numbers
        if self.max_value >= 10:
            badge_width = 25  # width for two-digit numbers
        if self.max_value >= 100:
            badge_width = 30  # width for three-digit numbers

        badge = Container(
            Text(
                display_count,
                color="white",
                weight=FontWeight.W_500,
                size=11,
                text_align="center",
            ),
            bgcolor=self.badge_color,
            border_radius=badge_width // 2,
            width=badge_width,
            height=badge_width,
            alignment=alignment.center,
        )
        if position == "top_left":
            badge.bottom = 26
            badge.left = 22
        elif position == "center_left":
            badge.top = 15
            badge.left = 22

        return badge


def main(page: Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(
        Badge(position="top_left"),
        Badge(
            cupertino_icons.CART,
            position="center_left",
        ),
        Badge(count=5, position="top_left"),
        Badge(count=15, position="top_left", max_value=9),
        Badge(count=105, position="center_left", max_value=99),
        Badge(count=1005, position="center_left", max_value=999),
    )


if __name__ == "__main__":
    app(target=main)
