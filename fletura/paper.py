import flet as ft
from flet import *


# A component for displaying content on an elevated surface
class Paper(Container):
    def __init__(
        self,
        outlined: bool = False,
        elevation: int = 1,
        alignment=ft.alignment.center,
        **kwargs,
    ) -> None:
        super().__init__(alignment=alignment**kwargs)
        self.elevation: int = elevation
        # Define the shadow parameters based on the distance
        self.shadow_params: dict = {
            0: (0, 0, 0, 0),
            1: (1, 2, 0.1, 1),
            2: (2, 4, 0.15, 2),
            3: (3, 6, 0.2, 3),
            4: (4, 8, 0.25, 4),
            8: (6, 10, 0.3, 8),
            12: (8, 12, 0.35, 12),
            16: (10, 14, 0.4, 16),
            24: (12, 14, 0.4, 16),
        }
        spread_radius, blur_radius, opacity, offset_y = self.shadow_params.get(
            self.elevation, (0, 0, 0, 0)
        )
        # Create the shadow based on the parameters
        shadows = [
            ft.BoxShadow(
                spread_radius=spread_radius,
                blur_radius=blur_radius,
                color=ft.colors.with_opacity(opacity, "black"),
                offset=ft.Offset(0, offset_y),
            )
        ]

        # Create the container with the specified shadow
        if outlined:
            self.border = border.all(width=2, color="#80868B")

        self.shadow = shadows


def main(page: Page):
    page.scroll = "always"
    # page.bgcolor = "white"
    page.theme_mode = "light"
    page.spacing = 50
    page.padding = 0
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    # Test the function with different distances
    distances = [0, 1, 2, 3, 4, 8, 12, 16, 24]
    for dist in distances:
        container = Paper(
            elevation=dist,
            width=200,
            height=50,
            bgcolor="white",
            outlined=True,
            content=ft.Text(f"Elevation {dist}", color="black"),
        )
        container.border_radius = 5
        page.add(container)
        if dist == 24:
            container.margin = margin.only(bottom=50)
        container.update()


if __name__ == "__main__":
    app(target=main)
