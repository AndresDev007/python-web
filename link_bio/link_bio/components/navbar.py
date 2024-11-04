import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "AndresDev",
            font_size="1.5em",            
        ),
        position="sticky",
        bg="lightblue",
        color="black",
        padding_x="16px",
        padding_y="8px",
        z_index="999",
        justify="center",
        height="50px",
    )
