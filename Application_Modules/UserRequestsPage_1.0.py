from shiny import ui, App
from typing import Any
from shiny.ui import div, p
import pandas as pd




choices = {"a": "Male", "b": "Female", "c": "Others"}

app_ui = ui.page_fluid(
    ui.panel_title("User Requests", "Window title"),
    ui.input_text("x1", "Latitude"),
    ui.input_text("x2", "Longitude"),
    ui.input_text("x3", "Cans"),
    ui.input_text("x4", "Glass_bottle"),
    ui.input_text("x4", "Plastic_bottle"),
    ui.input_password ("x5", "Cardboard",),
    ui.download_button('dwnld1','Submit'),
)

def server(input, output, session):
    @session.download()
    def dwnld1():
        path = Path(__file__).parent / "mtcars.csv"
        return str(path)



app = App(app_ui, server)
