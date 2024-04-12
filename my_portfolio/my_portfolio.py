"""Welcome to Reflex! This file outlines the steps to create a basic app."""



from rxconfig import config

import reflex as rx
from my_portfolio.components.navbar import nav_bar
from my_portfolio.components.footer import footer
from my_portfolio.pages.testpage import test
from my_portfolio.pages.projects import projects_page
from my_portfolio.pages.contact import contact



docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    
    """The app state."""






    
def index() -> rx.Component:
    return  rx.vstack(
                nav_bar(),
                rx.center(
                    rx.vstack(
                    rx.hstack(
                        rx.avatar(src='/Avatar.png', fallback='GK', size='8', radius='full'),
                        rx.vstack(
                            rx.heading("Giovanny Kelly", _as='h1', size="8" ,margin='0.3rem',),
                            rx.text("Freelance backend and software developer", margin='0.3rem',),
                            ),
                        ),
                    rx.heading("About Me", as_='h2', width="80%"),
                    rx.blockquote('''Im a Civil Engineer based on United States, which turns career paths, the love for innovations made me focus more on the development side of the things,
                                    lets build something awesome together!
                                  ''',
                                  width="80%"
                                  ),

                    rx.button(
                        "Check out my work!",
                        on_click=lambda: rx.redirect(docs_url),
                        size="4",
                    ),
                    rx.divider(size='4', width='90%'),
                    rx.text("Technologies", size="8"),
                    rx.stack(
                        rx.text("Python", size='5'),
                        rx.text("Django", size='5'),
                        rx.text("SQL", size='5'),
                        rx.text("Pandas", size='5'),
                        direction='row',
                        margin='1rem',
                    ),
                    rx.divider(size='4', width='90%'),
                    rx.text("Applications", size="8"),
                    rx.stack(
                        rx.text("Data Analysis", size='5'),
                        rx.text("Web Development", size='5'),
                        rx.text("Deep Learning", size='5'),
                        rx.text("Machine Learning", size='5'),
                        rx.text("APIs", size='5'),
                        direction='row',
                        spacing='6',
                        margin='1rem',
                    ),
                    rx.divider(size='4', width='90%'),
                    rx.text("Common Works", size="8"),
                    rx.stack(
                        rx.text("Ecommerce Solutions", size='5'),
                        rx.text("Personal & Business Website", size='5'),
                        rx.text("Data extraction", size='5'),
                        rx.text("Artificial Inteligence", size='5'),
                        direction='row',
                        spacing='6',
                        margin='1rem',
                    ),

                    align="center",
                    spacing="7",
                    font_size="1.4rem",
                    
                ),
    ),
    footer(),
    align_items = "center"
)


def testpage() -> rx.Component:
    return test()

app = rx.App(
    theme=rx.theme(
        appearance="dark", accent_color="orange", radius="large",
    )
)



app.add_page(index, title='Giovanny Kelly Portfolio', description='Giovanny Kelly Portfolio, im a fullstack python developer')
app.add_page(testpage)
app.add_page(projects_page, route='/projects', title='Giovanny Kelly Projects', description='Lets check my projects')
app.add_page(contact, route='/contact', title='Contact Me', description='Contact me about anything')


