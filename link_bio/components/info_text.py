import reflex as rx
from link_bio.styles.styles import Size as Size

# Componente que renderiza la experiencia.
def info_text(title:str, body:str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.span(
            title,
            font_weight="bold",
            color="blue"
        ),
        body,
        font_size=Size.MEDIUM.value,
    )

