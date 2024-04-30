import reflex as rx
from my_portfolio.components.navbar import nav_bar
from my_portfolio.components.footer import footer



def projects_page():
    return rx.vstack(
        nav_bar(),
rx.center(
    rx.vstack(
    rx.heading('My Projects', as_='h1', size='8', text_align='center', width='100%', margin='1rem',),
    rx.card(
    rx.image(src='/localxdeal.png'),
    rx.box(
        rx.heading('Ecommerce'),
        rx.text('This is a project set to display current available products for a local liquidator'),
        ),
        on_click=rx.redirect('https://www.localxdeal.com',external=True),
        cursor='pointer',
        align= "center",
            ),
        width='60%',
            ),
            align='center',
            min_height='75vh',
        ),
        footer(),
)
    
