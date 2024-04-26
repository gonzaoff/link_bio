import reflex as rx
from link_bio.components.links_buttom import link_button
from link_bio.components.title import title

# Navegador de pestañas
def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Planes de Entrenamiento",
            "Diseñado para las necesidades de cada persona.",
            "/planesEntrenamiento"),
        link_button(
            "Abordaje Nutricional",
            "¿Por que es importante?",
            "https://www.youtube.com/"),
        link_button(
            "Contactos",
            "Nutricore",
            "/"),
        width = "100%",
        align="center",
    )