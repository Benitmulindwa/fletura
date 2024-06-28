# Fletura
A material UI built with flet library

# Installation

A collection of reusable Flet components to enhance your application development.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
  - [CardMedia](#cardmedia)
  - [Dock](#dock)
  - [Timeline](#timeline)
  - [Rating](#rating)
  - [Paper](#paper)
  - [Neumorphic](#neumorphic)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This library provides a set of reusable Flet components designed to streamline the development of Flet-based applications. Each component is built with flexibility and ease of use in mind.

## Installation

To install the library, use pip:

```bash
pip install fletura
```
## Usage
Here is a basic example of how to use fletura
```python
import flet as ft
from fletura import CardMedia

def main(page):
card = CardMedia(
            image_src="https://th.bing.com/th/id/R.5e510c21c45cefceb127a2280c789b72?rik=2ddR7LkLmjAIFA&pid=ImgRaw&r=0",
            description="Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all continents except Antarctica",
            description_style=TextStyle(color="white"),
            actions=[
                TextButton("SHARE"),
                TextButton("LEARN MORE"),
            ],
            can_expand=True,
            long_description="A long description of the cardMedia content",
            title_style=TextStyle(color="white"),
        ),

    page.add(card)

ft.app(target=main)
```
# Components

## CardMedia
Cards are surfaces that display content and actions related to a single topic.
(inherits from Container)
### Props

- **image_src (str):** Image source
- **title (str):** The card title.
- **title_style (TextStyle):** Style to be applied on the card title
- **description (str):** The main content of the card.
- **description_style (TextStyle):** Style to be applied on both the card description and the long_description text(if provided)
- **long_descriprion (str):** Text to be displayed as a long description of the card content(**can_expand** must be True)
- **actions (list):** A list of action buttons or any controls for the card.
- **can_expand (bool):** This is applied only for cards with a long description, it gives the ability to expand
- **action_area (bool):** If True the entire card will be clickable, and the **on_click_action_area** event must be handled
- **width:** The cardMedia width, default value is 300

### Examples
```python
# CardMedia without a long description
CardMedia(
        image_src="https://th.bing.com/th/id/R.5e510c21c45cefceb127a2280c789b72?rik=2ddR7LkLmjAIFA&pid=ImgRaw&r=0",
        description="Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all continents except Antarctica",
        actions=[
            TextButton("SHARE"),
            TextButton("LEARN MORE"),
        ],
        description_style=TextStyle(color="white"),
        title_style=TextStyle(color="white"),
    ),
```
```python
# CardMedia component with action_area activated
CardMedia(
          image_src="https://th.bing.com/th/id/R.5e510c21c45cefceb127a2280c789b72?rik=2ddR7LkLmjAIFA&pid=ImgRaw&r=0",
          description="Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all continents except Antarctica",
          action_area=True,
          actions=[],
          description_style=TextStyle(color="white"),
          title_style=TextStyle(color="white"),
      ),
```
## Dock
Dock component puts a container on one of the corners of an other control(usually an icon)
### Props
- **dock_icon (str):** An icon, Mail icon is the default one
- **icon_color (str):** The icon color
- **dock_color (str):** color of the container
- **count (int):** The count to be displayed,
- **max_value (int):** the maximum value to be displayed,
- **position (str):** Postion of the top container(top_right, bottom_left, bottom_right) by default "top_left",

### Examples:
```python
Dock(position="top_left"), 
Dock(cupertino_icons.CART, position="center_left", count=105, max_value=99),
Dock(count=15, dock_color="purple500", position="top_left", max_value=9),
Dock(count=105, dock_color="blue", position="top_right", max_value=99),
Dock(count=1005, position="bottom_right", max_value=999)
```
## Rating
Ratings provide insight regarding others' opinions and experiences, and can allow the user to submit a rating of their own.
### Props
- **rating_type: (str)** "controlled","readonly" or "disabled".
- **max_value (int):** number of rating icons.
- **rating_value (float):** Works when "disabled" or "readonly" is selected.
- **rating_icon (str):** Rating icont, by default it's *icons.STAR_OUTLINE_OUTLINED*.
- **size (str):** The size of the rating icons,small "large".
- **color (str):** icon border color by default it's "colors.WHITE".
- **selection_color (str):** the icon_color when selected by default "colors.ORANGE".
- **selection_icon (str):** the icon when selected, by default it's  "icons.STAR".
- **half_icon (str):** takes in account float rating values Works when "disabled" or "readonly" is selected, by defaulf "icons.STAR_HALF".
- **on_hover_color (str):** color on hover by default "colors.ORANGE".
  
### Examples:

```python
Rating(
    rating_icon=icons.STAR_OUTLINE_OUTLINED,
    selection_icon=icons.STAR,
    max_value=5,
    rating_type=RatingType.CONTROLLED,
    ),
Rating(
  max_value=5,
  selection_icon=icons.STAR,
  rating_value=2.5,
  rating_type=RatingType.READONLY,
  size="large",
),
Rating(
  rating_icon=cupertino_icons.HEART,
  selection_icon=cupertino_icons.HEART_FILL,
  half_icon=icons.HEART_BROKEN_OUTLINED,
  max_value=5,
  rating_value=1.5,
  rating_type=RatingType.DISABLED,
),
```
## Paper
A component for displaying content on an elevated surface.
(inherits from container)
### Props
- **outlined (bool):** "True" if the Paper will be outlined otherwise False,
- **elevation (int):** Defines how much the Paper will be elevated (0,1,2,3,4,8,12,16 and 24) by default elevation = 1,
### Examples
```python
Paper(
      elevation=8,
      width=200,
      height=50,
      bgcolor="white",
      outlined=True,
      content=ft.Text(f"Elevation 8", color="black"),
)
```
## Neumorphic

# Contributing
Contributions are welcome! just PR

# License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
#
Thank you for using the Flet Components Library! If you have any questions or feedback, feel free to open an issue or submit a pull request.
