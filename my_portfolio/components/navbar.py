import reflex as rx
from my_portfolio.components.linked_buttons import linked_button
from my_portfolio.components.linked_icons import linked_icon
from my_portfolio.components.light_dark_button import light_dark_button


class NavbarState(rx.State):

    navbar: dict[str,str]= {"Home": "/", "Projects": "/projects", "Contact Me": "/contact"}

# '''
# Items in a dictionary in reflex can be accessed as list of key-value pairs. Using the color example, we can slightly modify the code to use dicts as shown below.
# '''

def display_desktopnav(item):
    return rx.text(item[0],
                   on_click= rx.redirect(item[1]),
                   cursor='pointer',
            )


def display_mobilenav(item):
    return rx.menu.item(
            item[0],
            on_click= lambda: rx.redirect(item[1]),
        )


def desktop_navbar() -> rx.Component:
    return rx.desktop_only(
                rx.hstack(
                    rx.heading("GiovDev", size='6',
                       on_click= lambda : rx.redirect('/'),
                       cursor='pointer',
                    ),
                    rx.spacer(),
                    rx.foreach(NavbarState.navbar, display_desktopnav),
                    rx.flex(
                    linked_icon('github','https://github.com/Gioak1993'),
                    linked_icon('linkedin', 'https://www.linkedin.com/in/giovanny-andrés-kelly-galindo/'),
                    light_dark_button(),
                    spacing='3',
                    ),
                    spacing="7",
                    margin="1rem",
                    
        ),
        width='100%',
    )

def mobile_navbar() -> rx.Component:

    return rx.mobile_and_tablet(
        rx.hstack(
            rx.heading("GiovDev", size='6',
                        on_click= lambda : rx.redirect('/'),
                        cursor='pointer',
                        ),
            rx.spacer(),
            light_dark_button(),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.icon('chevron-down'),
                        size='2',
                    ),
                ),
                rx.menu.content(
                    rx.foreach(NavbarState.navbar, display_mobilenav),
                    size='2',
                    align='center',
                    side='bottom',
                )
            ),
        ),
        width='100%',
        padding = "1.5rem",
    )


def nav_bar() -> rx.Component:
    return rx.stack(
        desktop_navbar(),
        mobile_navbar(),
        width='100%',
    )