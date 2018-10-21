import random
import json
import os
import time

from pico2d import *

import game_framework
import title_state
import pause_state
import main_state


name = "MainState"
boy = None
swallow = None
grass = None
font = None
global mx, my
mx=-1
my=-1
class Swallow:
    image1 = None
    image2 = None
    def __init__(self):
        self.y = random.randint(0,600)
        self.x = random.randint(0,800)
        self.frame = 0
        self.xdir = 1
        self.ydir = 1
        self.hp=1

        if Swallow.image1 == None:
            Swallow.image1 = load_image('swallow.png')

        if Swallow.image2 == None:
            Swallow.image2 = load_image('swallow2.png')

    def update(self):
        global mx, my
        self.frame = (self.frame + 1) % 5
        self.x += self.xdir
        self.y += self.ydir
        if self.hp>0:
            if self.x+30>=mx and self.x-30<=mx:
                if self.y+30>=600-my and self.y-30<=600-my:
                    self.hp-=1
                    mx=-1
                    my=-1

        if self.x >= 800:
            self.xdir = -1
        elif self.x <= 0:
            self.xdir = 1

        if self.y >= 600:
            self.ydir = -1
        elif self.y <= 0:
            self.ydir = 1

    def draw(self):
        if self.hp>0:
            if self.xdir==1:
                self.image1.clip_draw(self.frame * 42, 0, 42, 50, self.x, self.y)
            else:
                self.image2.clip_draw(self.frame * 42, 0, 42, 50, self.x, self.y)
class Gourd:
    def __init__(self):
        self.image = load_image('gourd_stand.png')
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
    global gourd
    gourd = Gourd()

def exit():
    global gourd
    del (gourd)


def pause():
    pass

def resume():
    pass


def handle_events():
    global mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            game_framework.push_state(main_state)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            mx = event.x
            my = event.y


def update():
    pass

def draw():
    clear_canvas()
    gourd.draw()
    time.sleep(0.005)
    update_canvas()