from guizero import App, Text, Waffle
import random

def destroy_dot(x,y):
    if (board[x,y].dotty):
        board[x,y].dotty=False
        board.set_pixel(x,y, "white")

def add_dot():
    x = random.randint(0,GRID_SIZE-1)
    y = random.randint(0,GRID_SIZE-1)
    
    while board[x,y].dotty == True:
        x = random.randint(0,GRID_SIZE-1)
        y = random.randint(0,GRID_SIZE-1)
    
    board[x,y].dotty = True
    board.set_pixel(x,y,"red")
    
    board.after(1000, add_dot)


GRID_SIZE = 5


app = App("Destroy the Dots")

instructions = Text(app, text="Click the dots to destroy them")

board = Waffle(app, width = GRID_SIZE, height= GRID_SIZE, command=destroy_dot)

board.after(1000, add_dot)
app.display()