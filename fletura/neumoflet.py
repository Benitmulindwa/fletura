from flet import *


class NeumorphicOval(Container):
    def __init__(self, diameter: int, **kwargs):
        super().__init__(
            width=diameter,
            height=diameter,
            border_radius=diameter * 2,
            shadow=[
                BoxShadow(
                    # spread_radius=1,
                    blur_radius=6,
                    color=colors.with_opacity(0.5, colors.WHITE),
                    offset=Offset(-1, -1),
                    blur_style=ShadowBlurStyle.INNER,
                ),
                BoxShadow(
                    # spread_radius=1,
                    blur_radius=6,
                    color=colors.with_opacity(0.5, colors.BLACK),
                    offset=Offset(1, 1),
                    blur_style=ShadowBlurStyle.OUTER,
                ),
            ],
            **kwargs,
        )
        self.alignment = alignment.center


class FlatContainer(Container):
    def __init__(self, width: int, height: int, **kwargs):
        super().__init__(
            bgcolor=colors.GREY_200,
            width=width,
            height=height,
            alignment=alignment.center,
            border_radius=10,
            shadow=[
                # BoxShadow(
                #     spread_radius=1,
                #     blur_radius=6,
                #     color=colors.with_opacity(0.5, colors.WHITE),
                #     offset=Offset(-3, -3),
                # ),
                BoxShadow(
                    spread_radius=1,
                    blur_radius=6,
                    color=colors.with_opacity(0.2, colors.BLACK),
                    offset=Offset(2, 2),
                ),
            ],
            **kwargs,
        )


class ConvexContainer(Container):
    def __init__(
        self,
        width: int,
        height: int,
        elevation: float = 0.0,
        shadow1_color: str = "white",
        shadow2_color: str = "black",
        **kwargs
    ):
        super().__init__(
            width=width,
            height=height,
            alignment=alignment.center,
            border_radius=10,
            gradient=LinearGradient(
                colors=["#cacaca", "#f0f0f0"],
                end=alignment.top_left,
                begin=alignment.center_right,
            ),
            shadow=[
                BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=colors.with_opacity(elevation, shadow1_color),
                    offset=Offset(1, 1),
                ),
                BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=colors.with_opacity(elevation, shadow2_color),
                    offset=Offset(-1, -1),
                ),
            ],
            **kwargs,
        )


class NeumorphicFloatingContainer(Container):
    def __init__(self, width: int, height: int, **kwargs):
        super().__init__(
            bgcolor=colors.GREY_200,
            width=width,
            height=height,
            alignment=alignment.center,
            border_radius=10,
            shadow=[
                BoxShadow(
                    spread_radius=1,
                    blur_radius=6,
                    color=colors.with_opacity(0.2, colors.WHITE),
                    offset=Offset(-5, -5),
                ),
                BoxShadow(
                    spread_radius=1,
                    blur_radius=6,
                    color=colors.with_opacity(0.2, colors.BLACK),
                    offset=Offset(5, 5),
                ),
            ],
            **kwargs,
        )


class NeumorphicCard(Container):
    def __init__(self, title: str, content_text: str, **kwargs):
        super().__init__(
            bgcolor=colors.GREY_200,
            width=250,
            height=150,
            padding=10,
            border_radius=20,
            shadow=[
                BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=colors.with_opacity(0.5, colors.WHITE),
                    offset=Offset(-5, -5),
                ),
                BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=colors.with_opacity(0.2, colors.BLACK),
                    offset=Offset(5, 5),
                ),
            ],
            content=Column(
                [
                    Text(title, size=20, weight=FontWeight.BOLD, color=colors.GREY_800),
                    Text(content_text, color=colors.GREY_600),
                ],
                alignment="center",
                spacing=10,
            ),
            **kwargs,
        )


def main(page: Page):
    page.bgcolor = colors.GREY_300
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 20
    page.theme_mode = "dark"

    neumorphic_flat_button = FlatContainer("Flat Button", height=50)
    neumorphic_pressed_button = ConvexContainer(
        width=200, height=50, content=Text("Convex Container")
    )
    neumorphic_floating_container = NeumorphicFloatingContainer(100, 100)
    neumorphic_card = NeumorphicCard("Neumorphic Card", "This is a neumorphic card.")

    neumorphic_oval = NeumorphicOval(
        content=Text("thin is a text", color="black"),
        diameter=150,
    )

    page.add(
        Column(
            [
                neumorphic_flat_button,
                neumorphic_pressed_button,
                neumorphic_floating_container,
                neumorphic_card,
                neumorphic_oval,
            ],
            alignment="center",
            spacing=20,
        )
    )


if __name__ == "__main__":
    app(target=main)
