import reflex as rx
from my_portfolio.components.linked_buttons import linked_button
from my_portfolio.components.linked_icons import linked_icon

class NavbarState(rx.State):

    navbar: dict[ str,str ]= {"Home": "/", "Projects": "/projects", "Contact Me": "/contact"}

'''
Items in a dictionary in reflex can be accessed as list of key-value pairs. Using the color example, we can slightly modify the code to use dicts as shown below.
'''

def display_nav(item):
    return rx.link(
        rx.text(item[0], color='white',
                           ),href=item[1]
)

def nav_bar() -> rx.Component:
    return rx.hstack(
            rx.heading("GiovDev"),
            rx.spacer(),
            rx.foreach(NavbarState.navbar, display_nav),
            rx.flex(
            linked_icon('github','https://github.com/Gioak1993'),
            linked_icon('linkedin', 'https://www.linkedin.com/in/giovanny-andrés-kelly-galindo/'),
            spacing='3',
            ),
            spacing="7",
            width="100%",
            position="flex",
            padding = "1.5em",
        )