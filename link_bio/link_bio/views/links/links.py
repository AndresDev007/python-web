import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button(
            "twitch", 
            "tutoriales semanales", 
            "https://twitch.tv"
        ),
        link_button(
            "youtube", 
            "tutoriales mensuales", 
            "https://youtube.com"
        ),
        link_button("github", 
                    "tutoriales anuales",
                    "https://github.com"
        ),
        align="center",
        width="100%"
    )
    