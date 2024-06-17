from flet import *


class Badge(Stack):
    def __init__(
        self, badge_icon: str = icons.MAIL, count: int = 9, position: str = "top_left"
    ):
        super().__init__()
        self.controls = [
            Container(
                Icon(badge_icon, color="white", size=30),
                height=50,
                width=50,
            ),
            self.create_badge(count, position),
        ]

    def create_badge(self, count: int, position: str):
        badge = Container(
            Text(
                f"{count}",
                color="white",
                weight=FontWeight.W_500,
                size=14,
                text_align="center",
            ),
            bgcolor="red",
            border_radius=10,
            width=20,
            height=20,
        )
        if position == "top_left":
            badge.top = 0
            badge.left = 0
        elif position == "middle_left":
            badge.top = 15  # Adjust based on the icon size and badge size
            badge.left = 0
        return badge


def main(page: Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(
        Badge(position="top_left"),
        Badge(position="middle_left"),
    )


if __name__ == "__main__":
    app(target=main)
