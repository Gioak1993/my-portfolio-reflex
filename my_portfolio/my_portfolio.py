"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
from my_portfolio.components.navbar import nav_bar
from my_portfolio.components.footer import footer
from my_portfolio.pages.index import index
from my_portfolio.pages.testpage import test
from my_portfolio.pages.projects import projects_page
from my_portfolio.pages.contact import contact




filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    
    """The app state."""




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


