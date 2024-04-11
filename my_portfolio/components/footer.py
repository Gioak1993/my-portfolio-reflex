from turtle import width
import reflex as rx
from my_portfolio.components.linked_buttons import linked_button

def footer () -> rx.Component:
    return rx.vstack(
            rx.divider(size='4', width='100%'),
            rx.text("Giovanny Kelly", size='3'),
            rx.hstack(
            linked_button('mail', 'https://google.com', 'giovk@giovdev.com'),
            linked_button('github','https://github.com/Gioak1993'),
            linked_button('linkedin', 'https://www.linkedin.com/in/giovanny-andrés-kelly-galindo/'),
            ),
            width="100%",
            padding='2rem',
        )
        
