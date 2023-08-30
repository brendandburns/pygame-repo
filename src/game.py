from pgzrun import *

alien = Actor('/images/alien.png')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20

alien.topright = 0, 10

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = '/images/alien_hurt.png'
    sound.play('/sounds/eep.wav')
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = '/images/alien.png'

go()