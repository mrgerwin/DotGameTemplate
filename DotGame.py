from guizero import App, Text, Waffle

app = App("Destroy the Dots")

instructions = Text(app, text="Click the dots to destroy them")

board = Waffle(app)

app.display()