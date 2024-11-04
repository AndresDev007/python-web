import reflex as rx
from enum import Enum

# Constants
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    BIG = "2em"

# Styles
BASE_STYLE = {
    "background_color": "#F7FAFC",
    "min_height": "100vh",

    rx.button: {
        "color": "black",
        "background_color": "lightgray",
        "text_transform": "uppercase",
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "cursor": "pointer",
        "gap": "30px",
    },
    rx.text: {
        "color": "black",
        "font_size": Size.DEFAULT.value,
        "text_align": "center",
    },
}

# Otra forma de definir propiedades css para un componente llamando directamente a style=button_title_style
button_title_style = dict ( # (no usado aun)
    font_size = Size.DEFAULT.value
)