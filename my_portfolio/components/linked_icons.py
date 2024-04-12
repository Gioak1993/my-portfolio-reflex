import reflex as rx

def linked_icon (icon:str, src:str, external = True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.flex(
                rx.icon(icon, spacing='1'),
                on_click=lambda: rx.redirect(
                    src,
                    external=external
                )
            )
        )
    )
