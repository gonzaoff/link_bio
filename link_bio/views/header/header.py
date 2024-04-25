import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import Size as Size

def header() -> rx.Component:
    return rx.box(
        rx.vstack(
        rx.hstack(
                rx.avatar(src="/logoMaxi.png", fallback="MG"),
                rx.vstack(  
                    rx.heading(
                        "Maximiliano Gudiño",
                        size="5"
                    ),
                    rx.hstack(
                        link_icon("https://www.instagram.com/mg.thetrainer"),
                        link_icon("mg.thetrainer23@gmail.com"),
                    ),
                    align_items="start"
                ),
                width="100%",
                align="center"
            ),
        rx.hstack(
                rx.avatar(src="/logoNutri.png", fallback="CG"),
                rx.vstack(  
                    rx.heading(
                        "Lic. Carolina De Giovanni",
                        size="5"
                    ),
                    rx.hstack(
                        link_icon("https://www.instagram.com/nutri.carodegiovanni"),
                        link_icon("carodegio@gmail.com"),

                        ),
                    align_items="start"
                ),
                width="100%",
                align="center"
            ),
            align_items="start"
        ),
        rx.flex(
            
        ),
        rx.text("Te damos la bienvenida a NUTRICORE, un proyecto creado para acompañarte en tu proceso de transformacion fisica y saludable, a través de un programa integral y personalizado que te brindara el acceso a un plan de entrenamiento y alimentacion"),     
        spacing=Size.BIG.value,
        align_items="start",
        align="center",    
    )
