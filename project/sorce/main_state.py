import random
import json
import os
import time

from pico2d import *

import game_framework
import title_state
import pause_state


name = "MainState"

boy = None
swallow = None
grass = None
font = None

class Swallow:
    image1 = None
    image2 = None
    def __init__(self):
        self.y = random.randint(0,600)
        self.x = random.randint(0,800)
        self.frame = 0
        self.xdir = 1
        self.ydir = 1
        if Swallow.image1 == None:
            Swallow.image1 = load_image('swallow.png')

        if Swallow.image2 == None:
            Swallow.image2 = load_image('swallow2.png')

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.x += self.xdir
        self.y += self.ydir
        if self.x >= 800:
            self.xdir = -1
        elif self.x <= 0:
            self.xdir = 1

        if self.y >= 600:
            self.ydir = -1
        elif self.y <= 0:
            self.ydir = 1

    def draw(self):
        if self.xdir==1:
            self.image1.clip_draw(self.frame * 42, 0, 42, 50, self.x, self.y)
        else:
            self.image2.clip_draw(self.frame * 42, 0, 42, 50, self.x, self.y)
class Gourd:
    def __init__(self):
        self.image = load_image('field_gourd.jpg')
        self.y = 100
        self.x = 100
    def draw(self):
        self.image.draw(self.x, self.y)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global gourd,birds
    gourd = Gourd()
    birds = [Swallow() for i in range(11)]

def exit():
    global gourd,birds
    del (birds)
    del (gourd)


def pause():
    pass

def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)


def update():
    for swallow in birds:
        swallow.update()

def draw():
    clear_canvas()
    gourd.draw()
    for swallow in birds:
        swallow.draw()
    time.sleep(0.005)
    update_canvas()





