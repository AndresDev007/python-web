import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "https://twitch.tv"),
        link_button("YouTube", "https://youtube.com"),
        link_button("Discord", "https://discord.gg"),
        link_button("GitHub", "https://github.com"),
        align="center"
    )
    