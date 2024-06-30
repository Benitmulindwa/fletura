from flet import *


class ShadowPosition:
    TOP_RIGHT: tuple = (5, -5)
    TOP_LEFT: tuple = (-5, -5)
    BOTTOM_RIGHT: tuple = (5, 5)
    BOTTOM_LEFT: tuple = (-5, 5)


class FlatContainer(Container):
    def __init__(self, height: int, **kwargs):
        super().__init__(
            bgcolor=colors.GREY_200,
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
        height: int,
        elevation: float = 0.0,
        shadow1_color: str = "white",
        shadow2_color: str = "black",
        border_radius=10,
        **kwargs,
    ):
        super().__init__(
            height=height,
            alignment=alignment.center,
            border_radius=border_radius,
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
                    offset=Offset(-1, -1),
                ),
                BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=colors.with_opacity(elevation / 2, shadow2_color),
                    offset=Offset(1, 1),
                ),
            ],
            **kwargs,
        )


class FloatingContainer(Container):
    def __init__(
        self,
        height: int,
        border_radius=10,
        bgcolor: str = colors.GREY_200,
        shadow1_color: str = colors.WHITE,
        shadow2_color: str = colors.BLACK,
        shadow_position: ShadowPosition = ShadowPosition.BOTTOM_RIGHT,
        **kwargs,
    ):
        super().__init__(
            bgcolor=bgcolor,
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
        width=100,
        height=100,
        border_radius=50,
        padding=padding.only(20),
        elevation=0.4,
        content=Text("Convex Container", color="black"),
    )
    neumorphic_floating_container = FloatingContainer(100, 100)
    neumorphic_card = FloatingContainer(
        content=Text("Neumorphic Card, This is a neumorphic card."),
        width=200,
        height=100,
    )

    page.add(
        Column(
            [
                neumorphic_flat_button,
                neumorphic_pressed_button,
                neumorphic_floating_container,
                neumorphic_card,
            ],
            alignment="center",
            spacing=20,
        )
    )


if __name__ == "__main__":
    app(target=main)
