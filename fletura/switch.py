from flet import *


class Switch(Container):
    def __init__(
        self,
        track_width: int = 60,
        track_height: int = 25,
        track_style: dict = {},
        active_track_content: Control = None,
        inactive_track_content: Control = None,
        thumb_width: int = 40,
        thumb_height: int = 40,
        active_thumb_content: Control = None,
        inactive_thumb_content: Control = None,
        default_thumb_content: Control = None,
        thumb_style: dict = None,
        active_color: str = "green",
        inactive_color: str = "grey",
        label: str = None,
        label_style: TextStyle = None,
        value: bool = False,
        on_hover: HoverEvent = None,
        on_change: ControlEvent = None,
    ):
        super().__init__(on_hover=on_hover)

        self.track_width = track_width
        self.track_height = track_height
        self.track_style = track_style
        self.active_track_content = active_track_content
        self.inactive_track_content = inactive_track_content
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        self.active_thumb_content = active_thumb_content
        self.inactive_thumb_content = inactive_thumb_content
        self.default_thumb_content = (
            inactive_thumb_content
            if default_thumb_content == None
            else default_thumb_content
        )
        self.thumb_style = thumb_style or {
            "bgcolor": "white",
            "border_radius": 20,
        }
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.label = label
        self.label_style = label_style
        self.on_change = on_change

        self.value = value  # initial state
        self.create_switch()

    def create_switch(self):
        # Create the switch components and layout.

        x_offset, y_offset = self.calculate_offsets()

        self.switch_thumb = Container(
            self.default_thumb_content,
            width=self.thumb_width,
            height=self.thumb_height,
            offset=transform.Offset(0 if self.value == False else -x_offset, -y_offset),
            animate_offset=animation.Animation(200, AnimationCurve.DECELERATE),
            **self.thumb_style,
        )

        self.switch_track = Container(
            self.inactive_track_content,
            width=self.track_width,
            height=self.track_height,
            bgcolor=self.inactive_color,
            border_radius=self.track_height / 2,
            **self.track_style,
        )
        self.switch_track.alignment = (
            alignment.center_left if self.value else alignment.center_right
        )

        self.switch_container = Container(
            content=Stack([self.switch_track, self.switch_thumb]),
            on_click=self.switch_changed,
            alignment=alignment.center,
        )
        self.label_text = Text(self.label, style=self.label_style)

        self.content = Row(
            [self.switch_container, self.label_text],
            alignment="center",
            vertical_alignment="center",
        )

        self.padding = padding.only(bottom=0, top=0)

    def calculate_offsets(self):
        # Calculate the offsets for centering the thumb.
        x_offset = (self.thumb_width - self.track_width) / (
            self.track_width / (self.track_width / self.thumb_width)
        )
        y_offset = (self.thumb_height - self.track_height) / (
            self.thumb_height / (self.track_height * 0.4) * self.track_height
        )
        return x_offset, y_offset

    def update_switch_state(self):

        x_offset, y_offset = self.calculate_offsets()

        self.switch_thumb.offset = (
            transform.Offset(-x_offset, -y_offset)
            if self.value
            else transform.Offset(0, -y_offset)
        )
        self.switch_thumb.content = (
            self.active_thumb_content if self.value else self.inactive_thumb_content
        )
        self.switch_track.bgcolor = (
            self.active_color if self.value else self.inactive_color
        )
        self.switch_track.content = (
            self.active_track_content if self.value else self.inactive_track_content
        )
        self.switch_track.alignment = (
            alignment.center_left if self.value else alignment.center_right
        )
        self.switch_thumb.update()
        self.switch_track.update()

    def switch_changed(self, e):
        self.value = not self.value
        self.update_switch_state()
        if self.on_change:
            self.on_change(self)
