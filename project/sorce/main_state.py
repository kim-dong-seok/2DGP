import random
import json
import os
import time

from pico2d import *

import game_framework
import title_state
import main_state2

name = "MainState"
boy = None
grass = None
windcursor = None
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
class Main_Background:
    def __init__(self):
        self.image = load_image('main_background.png')
        self.y = 300
        self.x = 400
    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, self.x,self.y,)


class Windcursor:
    image = None
    def __init__(self):
        self.frame = 0
        if Windcursor.image == None:
            self.image = load_image('cursor.png')

    def update(self):
        self.frame = (self.frame + 1) % 13


    def draw(self):
            self.image.clip_draw(self.frame * 30, 0, 30, 45, movemx, movemy)

class Money:
    image1=None
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        if Money.image1==None:
            self.image1 = load_image('0_9.png')

    def update(self):
        pass

    def draw(self):
        self.image1.clip_draw(((playermoney%10)+1)*97, 0, 97, 145,744,572, 17, 28)
        self.image1.clip_draw((((playermoney%100)//10)+1)*97, 0, 97, 145, 700, 572, 17, 28)
        self.image1.clip_draw((((playermoney%1000)//100)+1)*97, 0, 97, 145, 654, 572, 17, 28)
        self.image1.clip_draw((((playermoney%10000)//1000)+1)*97, 0, 97, 145, 638, 572, 17, 28)
        self.image1.clip_draw((((playermoney%100000)//10000)+1)*97, 0, 97, 145, 622, 572, 17, 28)
        self.image1.clip_draw((((playermoney%1000000)//100000)+1)*97, 0, 97, 145, 606, 572, 17, 28)
        self.image1.clip_draw((((playermoney%10000000)//1000000)+1)*97, 0, 97, 145, 590, 572, 17, 28)

class Main_UI:
    def __init__(self):
        self.image = load_image('main_ui.png')
        self.y = 300
        self.x = 400
    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, self.x,self.y,)


class Bird:
    def __init__(self):
        self.name=0
        self.hp=0
        self.sp=0
        self.expedition=0

    def update(self):
        pass

    def draw(self):
        pass


def enter():
    global main_ui,money,windcursor,main_background,cagebird
    main_ui = Main_UI()
    money=Money()
    main_background=Main_Background()
    windcursor=Windcursor()
    cagebird=[Bird() for i in range(6)]

def exit():
    global main_ui,money,windcursor,main_background,cagebird
    del (main_ui)
    del (money)
    del (windcursor)
    del(main_background)
    del(cagebird)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            game_framework.push_state(main_state2)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            mx = event.x
            my = 600-event.y
        elif event.type == SDL_MOUSEMOTION:
            movemx, movemy = event.x, 600 - event.y


def update():
    windcursor.update()


def draw():

    clear_canvas()
    hide_cursor()
    main_background.draw()
    main_ui.draw()
    money.draw()
    windcursor.draw()
    delay(0.03)
    update_canvas()





