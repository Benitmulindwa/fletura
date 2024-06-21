from flet import *


class TimelineEvent(Container):
    def __init__(
        self,
        title: str,
        title_style: TextStyle = None,
        description: str = None,
        description_style: TextStyle = None,
        timestamp: str = None,
        timestamp_style: TextStyle = None,
        icon: str = icons.EVENT,
        icon_size: int = 20,
        content_position: int = 8,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.title = title
        self.description = description
        self.timestamp = timestamp
        self.icon = icon
        self.icon_size = icon_size
        self.content_position = content_position
        self.title_style = title_style
        self.description_style = description_style
        self.timestamp_style = timestamp_style

        self.content = Row(
            [
                Column(
                    [
                        Container(
                            # Icon(self.icon, size=self.icon_size, color=colors.BLUE),
                            alignment=alignment.center,
                            padding=padding.all(5),
                            border=border.all(3, color="white"),
                            border_radius=10,
                        ),
                        Container(
                            width=2,
                            height=50,
                            bgcolor="white",
                            alignment=alignment.center,
                            margin=margin.only(top=5),
                        ),
                    ],
                    alignment="center",
                    horizontal_alignment="center",
                    spacing=0,
                ),
                Container(
                    Column(
                        [
                            Text(
                                self.title,
                                weight=FontWeight.BOLD,
                                size=16,
                                style=self.title_style,
                            ),
                            Text(
                                self.description, size=14, style=self.description_style
                            ),
                            Text(
                                self.timestamp,
                                size=12,
                                color=colors.GREY,
                                style=self.timestamp_style,
                            ),
                            Container(
                                height=self.content_position
                            ),  # A container to adjust the content position
                        ],
                        alignment="start",
                        spacing=5,
                    ),
                    padding=padding.only(0, top=0),
                    margin=margin.all(0),
                ),
            ],
            alignment="start",
            spacing=10,
        )

        self.margin = margin.only(top=10)


class Timeline(Container):
    def __init__(self, events: list, **kwargs):
        super().__init__(**kwargs)
        self.events = events

        self.content = Column(
            [TimelineEvent(**event) for index, event in enumerate(self.events)],
            alignment="start",
            spacing=0,
        )


def main(page: Page):
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"
    page.padding = 20

    events = [
        {
            "title": "Event 1",
            # "description": "This is the description for event 1.",
            # "timestamp": "2023-01-01 10:00 AM",
            # "icon": icons.EVENT,
            # "icon_size": 30,
            "content_position": 0,
        },
        {
            "title": "Event 2",
            "description": "This is the description for event 2.",
            "timestamp": "2023-02-01 12:00 PM",
            "icon": icons.CALENDAR_TODAY,
            "icon_size": 25,
        },
        {
            "title": "Event 3",
            "description": "This is the description for event 3.",
            "timestamp": "2023-03-01 02:00 PM",
            "icon": icons.DATE_RANGE,
            "icon_size": 20,
        },
    ]

    timeline = Timeline(events)

    page.add(timeline)


if __name__ == "__main__":
    app(target=main)
