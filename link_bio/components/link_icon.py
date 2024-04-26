import reflex as rx
import link_bio.styles.styles as styles

# Componente de los botones
def link_icon(url:str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="link"
        ),
        href=url,
        is_external=True,
    )