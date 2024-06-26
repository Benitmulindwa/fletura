from flet import *


class ShadowPosition:
    TOP_RIGHT: tuple = (5, -5)
    TOP_LEFT: tuple = (-5, -5)
    BOTTOM_RIGHT: tuple = (5, 5)
    BOTTOM_LEFT: tuple = (-5, 5)


class NeumorphicOval(Container):
    def __init__(self, diameter: int, **kwargs):
        super().__init__(
            width=diameter,
            height=diameter,
            border_radius=diameter // 2,
            bgcolor="blue",
            # gradient=RadialGradient(colors=["blue200", "blue900"]),
            shadow=[
                BoxShadow(
                    # spread_radius=1,
                    blur_radius=6,
                    color=colors.with_opacity(0.0, colors.BLACK12),
                    offset=Offset(-5, -5),
                    # blur_style=ShadowBlurStyle.INNER,
                ),
                BoxShadow(
                    # spread_radius=1,
                    blur_radius=6,
                    color=colors.with_opacity(0.5, colors.BLACK),
                    offset=Offset(5, 5),
                    # blur_style=ShadowBlurStyle.OUTER,
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


class FloatingContainer(Container):
    def __init__(
        self,
        width: int,
        height: int,
        border_radius=10,
        bgcolor: str = colors.GREY_200,
        shadow1_color: str = colors.WHITE,
        shadow2_color: str = colors.BLACK,
        shadow_position: ShadowPosition = ShadowPosition.BOTTOM_RIGHT,
        **kwargs
    ):
        super().__init__(
            bgcolor=bgcolor,
            width=width,
            height=height,
            alignment=alignment.center,
            border_radius=border_radius,
            shadow=[
                BoxShadow(
                    spread_radius=1,
                    blur_radius=6,
                    color=colors.with_opacity(0.2, shadow1_color),
                    offset=Offset(-shadow_position[0], -shadow_position[1]),
                ),
                BoxShadow(
                    spread_radius=1,
                    blur_radius=6,
                    color=colors.with_opacity(0.2, shadow2_color),
                    offset=Offset(*shadow_position),
                ),
            ],
            **kwargs,
        )


def main(page: Page):
    page.bgcolor = colors.GREY_300
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 20
    page.theme_mode = "light"

    neumorphic_flat_button = FlatContainer("Flat Button", height=50)
    neumorphic_pressed_button = ConvexContainer(
        width=200, height=50, content=Text("Convex Container", color="black")
    )
    neumorphic_floating_container = FloatingContainer(100, 100)
    neumorphic_card = FloatingContainer(
        content=Text("Neumorphic Card, This is a neumorphic card."),
        width=200,
        height=100,
    )

    neumorphic_oval = NeumorphicOval(
        content=Text("thin is a text", color="black"),
        diameter=100,
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
