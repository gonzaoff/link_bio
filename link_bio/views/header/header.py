import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.perfil import perfil
from link_bio.styles.styles import Size as Size

# Cabecera, perfil y descripcion 👌
def header() -> rx.Component:
    return rx.box(

        # Perfil Profe Maxi 💪
        perfil("Prof. Maximiliano Gudiño.","MG","+4","mg.thetrainer","mg.thetrainer@gmail.com"),

        # Perfil Nutri Caro 🧐
        perfil("Lic. Carolina Giovanni.","CG","+4","nutri.carodegiovanni","carogio@gmail.com"),
        

        # Descripcion 👀👀
        rx.text("Te damos la bienvenida a NUTRICORE, un proyecto creado para acompañarte en tu proceso de transformacion fisica y saludable, a través de un programa integral y personalizado que te brindara el acceso a un plan de entrenamiento y alimentacion"),     
        spacing=Size.BIG.value,
        align_items="start",
        align="center",    
        

    )
