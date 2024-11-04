import reflex as rx

def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(title, display="inline-block", margin_right="10px"),
            rx.text(title, display="inline-block"),
            rx.text(body, font_size="0.8em",),
            display="block",
            _hover={"background_color": "cyan"}
        ),
        href=url,
        is_external=True,
        width="100%"
    )