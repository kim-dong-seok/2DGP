import random
import json
import os
import time

from pico2d import *

import game_framework
import title_state
import pause_state
import main_state2

name = "MainState"
boy = None
swallow = None
grass = None
font = None
money=None
global playermoney
playermoney=99999999
global movemx, movemy
movemx=-1
movemy=-1
global mx, my
mx=-1
my=-1
class Money:
    image1=None
    image2=None
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        if Money.image1==None:
            self.image1 = load_image('0123456789.png')
        if Money.image2 == None:
            self.image2 = load_image('money.png')

    def update(self):
        self.frame = (self.frame + 1) % 8


    def draw(self):
        self.image2.clip_draw(0, 0, 547, 75, 625 ,575,350,50 )
        self.image1.clip_draw((playermoney%10)*24, 0, 24, 73, 708, 575, 15, 50)
        self.image1.clip_draw(((playermoney%100)//10)*24, 0, 24, 73, 663, 575, 15, 50)
        self.image1.clip_draw(((playermoney%1000)//100)*24, 0, 24, 73, 619, 575, 15, 50)
        self.image1.clip_draw(((playermoney%10000)//1000)*24, 0, 24, 73, 603, 575, 15, 50)
        self.image1.clip_draw(((playermoney%100000)//10000)*24, 0, 24, 73, 588, 575, 15, 50)
        self.image1.clip_draw(((playermoney%1000000)//100000)*24, 0, 24, 73, 573, 575, 15, 50)
        self.image1.clip_draw(((playermoney%10000000)//1000000)*24, 0, 24, 73, 557, 575, 15, 50)
        self.image1.clip_draw(240, 0, 264, 73, 541, 575, 15, 50)
        self.image1.clip_draw(240, 0, 264, 73, 526, 575, 15, 50)
        self.image1.clip_draw(240, 0, 264, 73, 511, 575, 15, 50)
class Swallow:
    image1 = None
    image2 = None
    imagehp = None
    def __init__(self):
        self.y = random.randint(0,500)
        self.x = random.randint(0,800)
        self.frame = 0
        self.xdir = 1
        self.ydir = 1
        self.hp=4

        if Swallow.image1 == None:
            Swallow.image1 = load_image('swallow.png')

        if Swallow.image2 == None:
            Swallow.image2 = load_image('swallow2.png')
        if Swallow.imagehp == None:
            Swallow.imagehp = load_image('hpbar.png')
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

        if self.y >= 500:
            self.ydir = -1
        elif self.y <= 0:
            self.ydir = 1

    def draw(self):

        if self.hp>0:
            if self.xdir==1:
                self.image1.clip_draw(self.frame * 42, 0, 42, 50, self.x, self.y)
            else:
                self.image2.clip_draw(self.frame * 42, 0, 42, 50, self.x, self.y)
        if self.hp < 3:
            if self.hp >= 1:
                self.imagehp.clip_draw(0, 0, 20, 10, self.x-20, self.y+20)
                if self.hp >= 2:
                    self.imagehp.clip_draw(0, 0, 20, 10, self.x, self.y + 20)
                    if self.hp >= 3:
                        self.imagehp.clip_draw(0, 0, 20, 10, self.x+20, self.y + 20)
class Gourd:
    def __init__(self):
        self.image = load_image('field_gourd.jpg')
        self.y = 100
        self.x = 100
    def draw(self):
        self.image.clip_draw(0, 0, 200, 200, 200, 200, 400, 400)
        self.image.clip_draw(0, 0, 200, 200, 600, 200, 400, 400)
        self.image.clip_draw(0, 0, 200, 200, 200, 600, 400, 400)
        self.image.clip_draw(0, 0, 200, 200, 600, 600, 400, 400)

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
    global gourd,birds,money
    gourd = Gourd()
    money=Money()
    birds = [Swallow() for i in range(11)]

def exit():
    global gourd,birds,money
    del (birds)
    del (gourd)
    del (money)


def pause():
    pass

def resume():
    pass


def handle_events():
    global mx, my
    global movemx,movemy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            game_framework.pop_state()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            mx = event.x
            my = event.y
        elif event.type == SDL_MOUSEMOTION:
            movemx, movemy = event.x, 600 - event.y


def update():
    for swallow in birds:
        swallow.update()




def draw():

    clear_canvas()
    image3 = load_image('fpscursor.png')
    hide_cursor()
    gourd.draw()
    money.draw()
    for swallow in birds:
        swallow.draw()

    image3.clip_draw(0, 0, 108, 109, movemx, movemy, 50, 50)
    time.sleep(0.005)
    update_canvas()





