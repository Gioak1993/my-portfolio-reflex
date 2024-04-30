import reflex as rx
from my_portfolio.components.navbar import nav_bar
from my_portfolio.components.footer import footer

class ClickChange(rx.State):

    colors: list[str] = [
        "black",
        "red",
        "green",
        "blue",
        "purple",
        
    ]

    index: int = 0

    def next_color(self):
        """An event handler to go to the next color."""
        # Event handlers can modify the base vars.
        # Here we reference the base vars `colors` and `index`.
        self.index = (self.index + 1) % len(self.colors)
    
    @rx.var
    def color(self) -> str:
        """A computed var that returns the current color."""
        # Computed vars update automatically when the state changes.
        return self.colors[self.index]
    

class ChangeText(rx.State):

    text:str="Click Me"

    def change_text(self):

        if self.text == "Click Me":
            self.text = "Opps, i just changed"
        else:
            self.text = "Click Me"


def test():
    return  rx.vstack(
            nav_bar(), 
            rx.center(
            rx.vstack(
                rx.text(" Hola, soy Giovanny Kelly, a civil engineer"),
                rx.button(ChangeText.text,
                on_click= [ChangeText.change_text, ClickChange.next_color],
                color = ClickChange.color,
                size="4",
                ),
                align_items="center",
            ),
            display = "flex",
            min_height="90vh",   
    ),
    footer(),
)
