import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="AD", size="6", radius="full"),
        rx.text("@AndresDev"),
        rx.text("Hola 👋 mi nombre es Andres"),
        rx.text("Soy un desarrollador de software full stack y experto en Python"),
        align="center"
    )