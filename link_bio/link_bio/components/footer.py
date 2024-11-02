import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.text(f"© {datetime.date.today().year} todos los derechos reservados ", rx.link("AndresDev", href="https://youtube.com", is_external=True)),
        align="center"
    )