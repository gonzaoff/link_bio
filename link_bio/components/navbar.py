import reflex as rx
from link_bio.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Nutricore",
        ),
        position="sticky",
        bg="lightgray",
        padding_y=Size.DEFAULT.value,
        padding_x=Size.SMALL.value,
        z_index="999",
        top="0"
    )