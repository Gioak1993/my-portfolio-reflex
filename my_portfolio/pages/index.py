
import reflex as rx

from my_portfolio.components.footer import footer
from my_portfolio.components.navbar import nav_bar
from my_portfolio.components.feature_text import featured_text

projects_url = "/projects"

def index() -> rx.Component:
    return  rx.vstack(
                nav_bar(),
                rx.center(
                    rx.vstack(
                        rx.flex(
                            rx.hstack(
                                rx.avatar(src='/Avatar.png', fallback='GK', size='8', radius='full', margin='0.3rem',),
                                rx.vstack(
                                    rx.heading("Giovanny Kelly", _as='h1', size="8" ,margin='0.3rem',),
                                    rx.text("Freelance backend and software developer", margin='0.3rem',),
                                ),
                            ),
                        ),
                    rx.heading("About Me", as_='h2', width="80%", margin='1rem',),
                    rx.blockquote('''Im a Civil Engineer based on United States, which turns career paths, the love for innovations made me focus more on the development side of the things,
                                    lets build something awesome together!
                                ''',
                                width='80%',
                                margin='1rem',
                                ),
                    rx.button(
                        "Check out my work!",
                        on_click=lambda: rx.redirect(projects_url),
                        size="4",
                        margin='1rem',
                    ),
                    rx.divider(size='4', width='90%', margin='1rem',),
                    rx.vstack(
                        rx.text("Technologies", size="8"),
                        rx.hstack(
                            featured_text("Python"),
                            rx.spacer(),
                            featured_text("Django"),
                            rx.spacer(),
                            featured_text("SQL"),
                            rx.spacer(),
                            featured_text("Pandas"),
                            margin='2rem',
                            width='90%',
                        ),
                        align='center',
                    ),
                    rx.divider(size='4', width='90%' ,margin='1rem',),
                    rx.vstack(
                        rx.text("Applications", size="8"),
                        rx.hstack(
                            featured_text("Data Analysis"),
        
                            featured_text("Web Development"),
    
                            featured_text("Deep Learning"),

                            featured_text("Machine Learning"),

                            featured_text("APIs"),
                            margin='2rem',
                            width='90%',
                        ),
                        align='center',
                    ),
                    rx.divider(size='4', width='90%', margin='1rem',),
                    rx.vstack(
                        rx.text("Common Works", size="8"),
                        rx.hstack(
                            featured_text("Ecommerce Solutions"),

                            featured_text("Personal & Business Website"),

                            featured_text("Data extraction"),

                            featured_text("Artificial Inteligence"),
                            margin='2rem',
                            width='90%',
                        ),
                        align='center',
                    ),
                    width='100%',
                    align='center',
                    ),
                ),
                footer(),
                min_width='fit-content',
                min_height='75vh',
        )
                    
