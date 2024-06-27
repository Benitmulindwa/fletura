from flet import *


class CardMedia(Container):
    def __init__(
        self,
        image_src: str,
        image_height: int = 140,
        can_expand: bool = False,
        actions: list = [],
        title: str = "Lizard",
        title_style: TextStyle = None,
        description: str = "",
        long_description: str = None,
        description_style: TextStyle = None,
        action_area: bool = False,
        on_click_action_area: ControlEvent = None,
        width=300,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.bgcolor = "black"
        self.width = width
        self.border_radius = 10
        self.padding = padding.only(bottom=10)

        self.expanded = False

        self.expanded_container = Container(
            ListView([Text(long_description, style=description_style)], auto_scroll=1),
            visible=False,
            padding=padding.only(10, right=10),
            margin=margin.only(bottom=10),
            # height=200,
        )
        self.image_container = Container(
            Image(
                src=image_src,
                fit="cover",
                height=image_height,
                width=self.width,
            ),
            alignment=alignment.center,
            margin=margin.all(0),
            width=400,
        )
        # A container to contain all the actions
        self.actions_row = Container(
            Row(
                [
                    *(action for action in actions),
                    Row(expand=True),
                    Container(
                        IconButton(icons.ARROW_DROP_DOWN, on_click=self.toggle_expand)
                        if can_expand == True
                        else None
                    ),
                ],
                spacing=0,
                alignment="start",
            ),
            margin=margin.only(top=5, right=10),
        )

        self.content = Column(
            [
                self.image_container,
                Container(
                    Column(
                        [
                            Container(
                                Text(
                                    f"{title}",
                                    size=20,
                                    weight=FontWeight.BOLD,
                                    style=title_style,
                                )
                            ),
                            Text(description, style=description_style),
                        ],
                        spacing=5,
                    ),
                    padding=padding.only(left=10, top=10, right=10),
                ),
                self.actions_row,
                self.expanded_container,
            ],
            spacing=0,
        )
        self.shadow = [
            BoxShadow(
                spread_radius=6,
                blur_radius=10,
                color=colors.with_opacity(0.3, "black"),
                offset=Offset(0, 8),
            )
        ]
        # These events are trigged only if the action_area property True
        self.on_click = on_click_action_area
        self.on_hover = self.action_area if action_area else None

    # when the dropdown iconbutton is clicked
    def toggle_expand(self, e):
        self.expanded = not self.expanded
        self.expanded_container.visible = self.expanded
        e.control.icon = icons.ARROW_DROP_UP if self.expanded else icons.ARROW_DROP_DOWN
        self.update()

    # trigged when the action_area is set to True & the Card is hovered by a cursor
    def action_area(self, e):
        e.control.opacity = 0.7 if e.data == "true" else 1.0
        e.control.update()


def main(page: Page):

    page.add(
        CardMedia(
            image_src="https://th.bing.com/th/id/R.5e510c21c45cefceb127a2280c789b72?rik=2ddR7LkLmjAIFA&pid=ImgRaw&r=0",
            description="Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all continents except Antarctica",
            actions=[TextButton("SHARE"), TextButton("LEARN MORE")],
            can_expand=True,
            # action_area=True,
            long_description="""To make the container expand when the drop-down icon is clicked, you can add a callback function that toggles the expansion of the description. This involves updating the visibility and possibly the size of the container when the icon is clicked. Here's how you can implement this:

Define a method to handle the expansion.
Add state to keep track of whether the card is expanded.
Update the icon button to toggle the expansion state.
""",
        )
    )


if __name__ == "__main__":
    app(target=main)
