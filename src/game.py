from pgzrun import *

WIDTH = 300
HEIGHT = 300

x = WIDTH / 2
y = HEIGHT / 2

dx = 5
dy = 2

def draw():
    screen.fill((128, 0, 0))
    screen.draw.filled_circle((x, y), 30, 'black')

def update():
    print('update!')
    global x, y, dx, dy
    x = x + dx
    y = y + dy

    if x > WIDTH or x < 0:
        dx = -dx
    if y > HEIGHT or y < 0:
        dy = -dy

go()