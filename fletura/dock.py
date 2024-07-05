from flet import *


class Dock(Container):
    def __init__(
        self,
        dock_icon: str = icons.MAIL,
        icon_color: str = "white",
        dock_color: str = "red",
        count: int = 4,
        max_value: int = 9,
        position: str = "top_left",
    ):
        super().__init__()
        self.max_value = max_value
        self.dock_color = dock_color
        self.content = Stack(
            [
                Container(
                    Icon(dock_icon, color=icon_color, size=30),
                    height=50,
                    width=60,
                    margin=margin.only(
                        left=-16 if "right" in position else 5, right=15
                    ),
                ),
                self.create_dock(count, position),
            ]
        )

        self.alignment = alignment.center

    def create_dock(self, count: int, position: str):
        display_count = f"{count}" if count <= self.max_value else f"{self.max_value}+"

        # Adjasting the top container size based on whether a single,2 or 3 digits number are given
        dock_width = 20  # default width for single-digit numbers
        if self.max_value >= 10:
            dock_width = 25  # width for two-digit numbers
        if self.max_value >= 100:
            dock_width = 30  # width for three-digit numbers

        dock = Container(
            Text(
                display_count,
                color="white",
                weight=FontWeight.W_500,
                size=11,
                text_align="center",
            ),
            bgcolor=self.dock_color,
            border_radius=dock_width // 2,
            width=dock_width,
            height=20,
            alignment=alignment.center,
        )
        if position == "top_right":
            dock.bottom = 26
            dock.left = 22
        elif position == "center_left":
            dock.top = 15
            dock.left = 22
        elif position == "bottom_right":
            dock.top = 26
            dock.left = 22
        elif position == "bottom_left":
            dock.top = 26
            dock.right = 50
        else:
            dock.bottom = 26
            dock.right = 50

        return dock


def main(page: Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(
        Dock(position="top_left"),
        Dock(cupertino_icons.CART, position="top_right", count=105, max_value=99),
        Dock(count=15, dock_color="purple500", position="top_left", max_value=9),
        Dock(count=105, dock_color="blue", position="top_right", max_value=99),
        Dock(count=1005, position="bottom_right", max_value=999),
    )


if __name__ == "__main__":
    app(target=main)
