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
