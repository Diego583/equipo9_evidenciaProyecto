"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from tkinter.messagebox import YES
from turtle import *

from freegames import line

grid_array = ["0", "0", "0","0", "0", "0","0", "0", "0"]

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)
    color('red')


def drawx(x, y):
    """Draw X player."""
    line(x, y, x + 50, y + 50)
    line(x, y + 50, x + 50, y)


def drawo(x, y):
    """Draw O player."""
    up()
    goto(x+30, y)
    down()
    circle(30)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 160


state = {'player': 0}
players = [drawx, drawo]

def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player
    if x == -160 and y == 106:
        if grid_array[0] == "0":
            print("Not taken")
        else:
            print("Taken")

    elif x == -27 and y == 106:
        if grid_array[1] == "0":
            grid_array[1] = 1
            print("Not taken")
        else:
            print("Taken")

    elif x == 106 and y == 106:
        if grid_array[2] == "0":
            grid_array[2] = 1
            print("Not taken")

        else:
            print("Taken")

    elif x == -160 and y == -27:
        if grid_array[3] == "0":
            grid_array[3] = 1
            print("Not taken")

        else:
            print("Taken")

    elif x == -27 and y == -27:
        if grid_array[4] == "0":
            grid_array[4] = 1
            print("Not taken")

        else:
            print("Taken")

    elif x == 106 and y == -27:
        if grid_array[5] == "0":
            grid_array[5] = 1
            print("Not taken")

        else:
            print("Taken")

    elif x == -160 and y == -160:
        if grid_array[6] == "0":
            grid_array[6] = 1
            print("Not taken")

        else:
            print("Taken")

    elif x == -27 and y == -160:
        if grid_array[7] == "0":
            grid_array[7] = 1
            print("Not taken")

        else:
            print("Taken")

    elif x == 106 and y == -160:
        if grid_array[8] == "0":
            grid_array[8] = 1
            print("Not taken")

        else:
            print("Taken")


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()