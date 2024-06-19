from flet import *


class CardMedia(Container):
    def __init__(
        self,
        actions: list = [TextButton("SHARE"), TextButton("LEARN MORE")],
        title: str = "Lizard",
    ):
        super().__init__()

        self.bgcolor = "black"
        self.width = 300
        self.border_radius = 10
        self.padding = padding.only(bottom=10)
        self.content = Column(
            [
                Container(
                    Image(
                        src="https://th.bing.com/th/id/R.5e510c21c45cefceb127a2280c789b72?rik=2ddR7LkLmjAIFA&pid=ImgRaw&r=0",
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
                                Text(f"{title}", size=20, weight=FontWeight.BOLD)
                            ),
                            Text(
                                "Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all continents except Antarctica"
                            ),
                        ],
                        spacing=5,
                    ),
                    padding=padding.only(left=10, top=10, right=10),
                ),
                Container(
                    Row([action for action in actions], spacing=0, alignment="start"),
                    margin=margin.only(top=5),
                ),
            ],
            spacing=0,
        )


def main(page: Page):
    page.bgcolor = "blue700"
    page.add(CardMedia())


if __name__ == "__main__":
    app(target=main)
