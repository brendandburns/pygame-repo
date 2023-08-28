from pgzrun import *

WIDTH = 300
HEIGHT = 300

x = WIDTH / 2
y = HEIGHT / 2

dx = 5
dy = 2

alien = Actor('/images/alien.png')
alien.pos = 100, 56

print("pygame-zero!")

def draw():
    screen.fill((128, 0, 0))
#    screen.draw.filled_circle((x, y), 30, 'black')
    alien.draw()

def update():
    global x, y, dx, dy
    x = x + dx
    y = y + dy

    if x > WIDTH or x < 0:
        dx = -dx
    if y > HEIGHT or y < 0:
        dy = -dy
    
    alien.pos = x, y

def on_mouse_down(pos, button):
    if alien.collide_point(pos):
        print("Eek!")
    else:
        print("You missed me!")

def on_key_down(key):
    print(key)

go()