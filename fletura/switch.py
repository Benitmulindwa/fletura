from flet import *


def main(page: Page):
    def button_clicked(e):
        t.value = f"Switch values are: {c1.value}, {c2.value}, {c3.value}, {c4.value}."
        page.update()

    t = Text()
    c1 = Switch(
        label="Unchecked switch",
        value=False,
        focus_color="pink",
        track_outline_color="pink",
        width=50,
        thumb_icon={
            MaterialState.SELECTED: icons.LIGHT_MODE,
            MaterialState.DEFAULT: icons.DARK_MODE,
        },
    )
    c2 = Switch(label="Checked switch", value=True)
    c3 = Switch(label="Disabled switch", disabled=True)
    c4 = Switch(
        label="Switch with rendered label_position='left'",
        label_position=LabelPosition.LEFT,
    )
    b = ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(c1, c2, c3, c4, b, t)


app(target=main)
