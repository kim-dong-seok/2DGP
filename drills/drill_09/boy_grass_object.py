from pico2d import *
from random import *

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:

    def __init__(self):
        self.x = randrange(0,600,30)
        self.y = 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class RandomBall:

    def __init__(self):
        self.x = 400
        self.y = 600
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 75:
            self.y -= 5

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():

    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
team = [Boy() for i in range(11)]
grass = Grass()
ball= RandomBall()
running = True;
# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()
    ball.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    ball.draw()
    update_canvas()
    delay(0.05)
# finalization code
close_canvas()