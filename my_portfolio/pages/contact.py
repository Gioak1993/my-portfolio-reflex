import reflex as rx
from my_portfolio.components.navbar import nav_bar
from my_portfolio.components.footer import footer

def contact() -> rx.Component:
    return rx.vstack(
        nav_bar(),
        rx.center(
        rx.heading('Contact Me', as_='h1',), #width='100%'#,),
        
        text_align='center',
        width='100%',
        min_height='75vh',
    ),
    footer(),
)