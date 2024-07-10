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
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.content = (
            Icon(
                icon,
                size=icon_size,
                color=icon_color,
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
        **kwargs,
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
