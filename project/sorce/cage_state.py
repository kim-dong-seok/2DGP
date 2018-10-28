import random
import json
import os
import time

from pico2d import *

import game_framework
import main_state
import main_state2

name = "MainState"
boy = None
grass = None
windcursor = None
font = None
money=None


class Windcursor:
    image = None
    def __init__(self):
        self.frame = 0
        if Windcursor.image == None:
            self.image = load_image('cursor.png')

    def update(self):
        self.frame = (self.frame + 1) % 13


    def draw(self):
            self.image.clip_draw(self.frame * 30, 0, 30, 45, main_state.movemx, main_state.movemy)

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
        self.image1.clip_draw(((main_state.playermoney%10)+1)*97, 0, 97, 145,692,568, 17, 28)
        self.image1.clip_draw((((main_state.playermoney%100)//10)+1)*97, 0, 97, 145, 642, 568, 17, 28)
        self.image1.clip_draw((((main_state.playermoney%1000)//100)+1)*97, 0, 97, 145, 584, 568, 17, 28)
        self.image1.clip_draw((((main_state.playermoney%10000)//1000)+1)*97, 0, 97, 145, 566, 568, 17, 28)
        self.image1.clip_draw((((main_state.playermoney%100000)//10000)+1)*97, 0, 97, 145, 548, 568, 17, 28)
        self.image1.clip_draw((((main_state.playermoney%1000000)//100000)+1)*97, 0, 97, 145, 530, 568, 17, 28)
        self.image1.clip_draw((((main_state.playermoney%10000000)//1000000)+1)*97, 0, 97, 145, 512, 568, 17, 28)

class Main_UI:
    def __init__(self):
        self.image = load_image('main_ui.png')
        self.y = 300
        self.x = 400
    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, self.x,self.y,)


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
    global main_ui,money,windcursor
    main_ui = Main_UI()
    money=Money()
    windcursor=Windcursor()


def exit():
    global main_ui,money,windcursor
    del (main_ui)
    del (money)
    del (windcursor)

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            game_framework.pop_state()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            main_state.mx = event.x
            main_state.my = 600-event.y
        elif event.type == SDL_MOUSEMOTION:
            main_state.movemx, main_state.movemy = event.x, 600 - event.y


def update():
    windcursor.update()


def draw():

    clear_canvas()
    hide_cursor()
    main_ui.draw()
    money.draw()
    windcursor.draw()
    delay(0.03)
    update_canvas()




