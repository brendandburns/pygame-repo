from pgzrun import *
from util import Background

WIDTH = 800
HEIGHT = 600

alien = Actor('/images/alien.png')
alien.pos = WIDTH/2, HEIGHT/2
alien.dx = 5
alien.dy = 2

bg = Background('/images/bg.jpg', WIDTH, HEIGHT)

def draw():
    bg.draw()
    alien.draw()

def update():
    x = alien.pos[0] + alien.dx
    y = alien.pos[1] + alien.dy

    if x > WIDTH or x < 0:
        alien.dx = -alien.dx
    if y > HEIGHT or y < 0:
        alien.dy = -alien.dy

    alien.angle += 1
    
    alien.pos = x, y

def on_mouse_down(pos, _button):
    if alien.collide_point(pos):
        print("Eek!")
    else:
        print("You missed me!")

def on_key_down(key):
    pass

def on_key_up(key):
    pass

go()
