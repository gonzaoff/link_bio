import reflex as rx
import datetime

# Footer o pie de pagina, marca personal #Sibotec👌
def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="/favicon.ico"),

        # Con datetime obtengo el año actual 🗓️
        rx.link(f"© 2023-{datetime.date.today().year} Sibotec by Gonzalo Sibolich", href="https://www.instagram.com/sibofit", is_external=True),
        align="center",
        size=""
    )