from turtle import width
import reflex as rx

def linked_button (icon:str, src:str, text='', external = True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.button(
                rx.icon(icon),
                text,
                on_click=rx.redirect(
                    src,
                    external=external
                )
            )
        )
)
