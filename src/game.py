import pgzrun
import random
from pgzrun import *


TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

# These constants control the difficulty of the game
GAP = 230
GRAVITY = 0.3
FLAP_STRENGTH = 6.5
SPEED = 3

bird = Actor('/images/bird1.png', (75, 200))
bird.dead = False
bird.score = 0
bird.vy = 0

bg = Actor('/images/background.png', (WIDTH//2, HEIGHT//2))

# TODO: storage support here
# storage.setdefault('highscore', 0)
storage = {}
storage['highscore'] = 0

def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.bottomleft = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.topleft = (WIDTH, pipe_gap_y + GAP // 2)

# FIX: kwargs for Actor constructor
pipe_top = Actor('/images/top.png') #, anchor=('left', 'bottom'))
pipe_bottom = Actor('/images/bottom.png') #, anchor=('left', 'top'))
reset_pipes()  # Set initial pipe positions.


def update_pipes():
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()
        if not bird.dead:
            bird.score += 1
            if bird.score > storage['highscore']:
                storage['highscore'] = bird.score


def update_bird():
    uy = bird.vy
    bird.vy += GRAVITY
    bird.y += (uy + bird.vy) / 2
    bird.x = 75

    if not bird.dead:
        if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
            bird.dead = True
            bird.image = '/images/birddead.png'
        else:
            if bird.vy < -3:
                bird.image = '/images/bird2.png'
            else:
                bird.image = '/images/bird1.png'

    if not 0 < bird.y < 720:
        bird.y = 200
        bird.dead = False
        bird.score = 0
        bird.vy = 0
        reset_pipes()


def update():
    update_pipes()
    update_bird()


def on_key_down():
    if not bird.dead:
        bird.vy = -FLAP_STRENGTH


def draw():
    screen.clear()
    # TODO: fix blit
    # screen.blit('/images/background.png', (0, 0))
    bg.draw()
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()
    screen.draw.text(str(bird.score), (WIDTH // 2, 50), color='white', fontsize=70)
# TODO: keyword args for pos, midtop, shadow in text
#    screen.draw.text(
#        str(bird.score),
#        color='white',
#        midtop=(WIDTH // 2, 10),
#        fontsize=70,
#        shadow=(1, 1)
#    )
    screen.draw.text(
        "Best: {}".format(storage['highscore']),
        pos=(WIDTH // 2, HEIGHT - 50),
        # TODO: support array as tuple
        # color=(255, 255, 255),
        color='blue',
        midbottom=(WIDTH // 2, HEIGHT - 10),
        fontsize=30,
        shadow=(1, 1)
    )


pgzrun.go()