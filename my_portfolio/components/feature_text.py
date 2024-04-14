import reflex as rx

def featured_text(text:str) -> rx.Component:
    return rx.text(text,
                   size='5',
                   text_align='center'
                   )