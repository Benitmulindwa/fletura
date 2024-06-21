from flet import *


class TimelineDot(Container):
    def __init__(
        self,
        icon: str = None,
        icon_size: int = 0,
        icon_color: str = colors.WHITE,
        dot_size: int = 5,
        dot_border_radius: int = 50,
        border: Border = border.all(3, color="white"),
        **kwargs
    ):
        super().__init__(**kwargs)
        self.content = (
            Icon(
                kwargs.get(icon),
                size=kwargs.get(icon_size),
                color=kwargs.get(icon_color, colors.BLUE),
            )
            if icon != None
            else None
        )
        self.alignment = alignment.center
        self.padding = padding.all(dot_size)
        self.border = border
        self.border_radius = dot_border_radius


class TimelineSeparator(Container):
    def __init__(
        self, color: str = colors.WHITE, width: int = 2, height: int = 50, **kwargs
    ):
        super().__init__(**kwargs)
        self.content = Container(
            width=width,
            height=height,
            bgcolor=color,
            alignment=alignment.center,
        )


class TimelineEvent(Container):
    def __init__(
        self,
        title: str,
        dot_props: dict = {},
        separator_props: dict = {},
        title_style: TextStyle = None,
        description: str = None,
        description_style: TextStyle = None,
        timestamp: str = None,
        timestamp_style: TextStyle = None,
        content_position: int = 8,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.title = title
        self.description = description
        self.timestamp = timestamp

        self.content_position = content_position
        self.title_style = title_style
        self.description_style = description_style
        self.timestamp_style = timestamp_style

        self.dot_props = dot_props
        self.separator_props = separator_props

        self.content = Row(
            [
                Column(
                    [
                        TimelineDot(**self.dot_props),
                        TimelineSeparator(**self.separator_props),
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
            "description": "This is the description for event 1.",
            "timestamp": "2023-01-01 10:00 AM",
            # "icon": icons.EVENT,
            # "icon_size": 30,
            "dot_props": {
                # "border_color": "red",
                # "border_radius": 2,
                # "dot_border_radius": 0,
                "border": border.all(2, color="blue"),
            },
            "content_position": 0,
            "separator_props": {
                "color": colors.GREEN_500,
                # "width": 3,
                "height": 70,
                "margin": margin.only(top=5),
            },
            "content_position": 25,
        },
        {
            "title": "Event 2",
            "description": "This is the description for event 2.",
            "timestamp": "2023-02-01 12:00 PM",
            # "icon": icons.CALENDAR_TODAY,
            # "icon_size": 25,
            "dot_props": {
                # "border_color": "red",
                # "border_radius": 2,
                # "dot_border_radius": 0,
                "border": border.all(2, color="red"),
            },
            "content_position": 0,
            "separator_props": {
                # "color": colors.BLUE,
                # "width": 3,
                "height": 70,
                "margin": margin.only(top=5),
            },
            "content_position": 25,
        },
        {
            "title": "Event 3",
            "description": "This is the description for event 3.",
            "timestamp": "2023-03-01 02:00 PM",
            # "icon": icons.DATE_RANGE,
            # "icon_size": 20,
            "dot_props": {
                # "border_color": "red",
                # "border_radius": 2,
                # "dot_border_radius": 0,
                "border": border.all(2, color="green"),
            },
            "content_position": 0,
            "separator_props": {
                # "color": colors.BLUE,
                # "width": 3,
                "height": 70,
                "margin": margin.only(top=5),
            },
            "content_position": 20,
        },
    ]

    timeline = Timeline(events)

    page.add(timeline)


if __name__ == "__main__":
    app(target=main)
