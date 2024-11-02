import reflex as rx

def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            text, 
            style={
                "cursor": "pointer"
                }
            ), 
        href=url,
        is_external=True
        )