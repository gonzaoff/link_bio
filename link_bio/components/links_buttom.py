import reflex as rx
import link_bio.styles.styles as styles

# Componente de las pestañas
def link_button(text: str,body: str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow-right",
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin_y="10px"
                ),
                rx.vstack(
                    rx.text(text,style=styles.button_title_style),
                    rx.text(body,style=styles.button_body_style),
                    
                )
            ),
        ),

        as_child = True,

        href=url,
        is_external=True,
        width="100%"
        
    )
    
    