import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="AD", size="6", radius="full", variant="solid", high_contrast=True),
        rx.text("@AndresDev"),
        rx.text("Hola 👋 mi nombre es Andrés"),
        rx.text("Soy un desarrollador de software full stack y experto en Python"),
        align="center"
    )