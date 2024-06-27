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
            description_style=TextStyle(
                color="white"
            ),
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
### Props

- **image_src (str):** Image source
- **title (str):** The card title.
- **title_style (TextStyle):** Style to be applied on the card title
- **description (str):** The main content of the card.
- **description_style (TextStyle):** Style to be applied on both the card description and the long_description text(if provided)
- **long_descriprion (str):** Text to be displayed as a long description of the card content(**can_expand** must be True)
- **actions (list):** A list of action buttons for the card.
- **can_expand (bool):** This applied only for cards with a long description, it gives the ability to expand
- **action_area (bool):** If True the entire card will be clickable, and the **on_click_action_area** event must be handled
- **width:** The cardMedia width, default value is 300

### Example
```python
# CardMedia without a long description
CardMedia(
        image_src="https://th.bing.com/th/id/R.5e510c21c45cefceb127a2280c789b72?rik=2ddR7LkLmjAIFA&pid=ImgRaw&r=0",
        description="Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all continents except Antarctica",
        actions=[
            TextButton("SHARE"),
            TextButton("LEARN MORE"),
        ],
        description_style=TextStyle(
            color="white"
        ),
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
          description_style=TextStyle(
              color="white"
          ),
          title_style=TextStyle(color="white"),
      ),
```
