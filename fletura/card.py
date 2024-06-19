from flet import *


class CardMedia(Container):
    def __init__(
        self,
        image_src: str,
        can_expand: bool = False,
        actions: list = [TextButton("SHARE"), TextButton("LEARN MORE")],
        title: str = "Lizard",
        title_style: TextStyle = None,
        description: str = "",
        description_style: TextStyle = None,
    ):
        super().__init__()

        self.bgcolor = "black"
        self.width = 300
        self.border_radius = 10
        self.padding = padding.only(bottom=10)
        # self.blur = 30
        self.expanded = False

        self.expanded_container = Container(
            Text(
                """To make the container expand when the drop-down icon is clicked, you can add a callback function that toggles the expansion of the description. This involves updating the visibility and possibly the size of the container when the icon is clicked. Here's how you can implement this:

Define a method to handle the expansion.
Add state to keep track of whether the card is expanded.
Update the icon button to toggle the expansion state.
Here's the complete code for the CardMedia class and the main function:
Define a method to handle the expansion.
Add state to keep track of whether the card is expanded.
Update the icon button to toggle the expansion state.
Here's the complete code for the CardMedia class and the main function:"""
            ),
            visible=False,
            padding=padding.only(10, right=10),
        )

        self.content = Column(
            [
                Container(
                    Image(
                        src=image_src,
                        fit="cover",
                        # border,
                        height=140,
                        width=self.width,
                    ),
                    alignment=alignment.center,
                    margin=margin.all(0),
                    # height=140,
                    width=400,
                ),
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
                Container(
                    Row(
                        [
                            *(action for action in actions),
                            Row(expand=True),
                            Container(
                                IconButton(
                                    icons.ARROW_DROP_DOWN, on_click=self.toggle_expand
                                )
                                if can_expand == True
                                else None
                            ),
                        ],
                        spacing=0,
                        alignment="start",
                    ),
                    margin=margin.only(top=5, right=10),
                ),
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
        # self.on_click = lambda _: print("okokokkk")

    def toggle_expand(self, e):
        self.expanded = not self.expanded
        self.expanded_container.visible = self.expanded
        e.control.icon = icons.ARROW_DROP_UP if self.expanded else icons.ARROW_DROP_DOWN
        self.update()


def main(page: Page):

    page.add(
        CardMedia(
            image_src="https://th.bing.com/th/id/R.5e510c21c45cefceb127a2280c789b72?rik=2ddR7LkLmjAIFA&pid=ImgRaw&r=0",
            description="Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all continents except Antarctica",
            can_expand=True,
        )
    )


if __name__ == "__main__":
    app(target=main)
