import flet as ft
from flet import *


# A component for displaying content on an elevated surface
class Paper(Container):
    def __init__(
        self,
        bgcolor: str,
        elevation: int = 1,
        content: Control = None,
        on_click: ControlEvent = None,
    ) -> None:
        super().__init__(content=content, bgcolor=bgcolor, on_click=on_click)
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
        self.width = 200
        self.height = 50
        self.padding = ft.padding.all(10)
        self.alignment = ft.alignment.center

        self.shadow = shadows

        # self.update()
        # return elevated_container


def main(page: Page):
    page.scroll = "always"
    page.bgcolor = "white"
    page.spacing = 50
    page.padding = 0
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    # Test the function with different distances
    distances = [0, 1, 2, 3, 4, 8, 12, 16, 24]
    for dist in distances:
        container = Paper(
            elevation=dist,
            bgcolor="white",
            content=ft.Text(f"Elevation {dist}", color="black"),
        )
        # container.on_click = lambda _: print("clicked")
        page.add(container)
        if dist == 24:
            container.margin = margin.only(bottom=50)
        container.update()


if __name__ == "__main__":
    app(target=main)
