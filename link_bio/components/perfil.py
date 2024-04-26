import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text

# Funcion creadora de perfiles 📷📷
def perfil(name:str,iniciales: str,experiencia:str,ig: str,correo: str) -> rx.Component:
    # Primero, retorna un stack vertical
    return rx.box(
        rx.vstack(
        # Segundo, retortna un stack horizontal
            rx.hstack(
                # Reenderiza el avatar con sus atributos definidos.
                rx.avatar(src="", fallback=iniciales, color_scheme="ruby",radius="full",size="7"),
                # Retorna un stack vertical donde se encuentra el nombre y los botones a sus redes sociales
                rx.vstack(  
                    rx.heading(
                        name,
                        size="5"
                    ),
                    rx.hstack(
                        link_icon(f"https://www.instagram.com/{ig}"),
                        link_icon(correo),

                    ),
                    align_items="start",
                    
                ),
                width="100%",
                align="center"

            ),
        ),
        rx.flex(
            info_text(experiencia, "años de experiencia")
        ),
    )