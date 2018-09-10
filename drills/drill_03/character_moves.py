from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90
angle=0
r = 210
while True:
    while (30+x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    while (45+y < 600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        y = y + 2
        delay(0.01)
    while (x-30 > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        x = x - 2
        delay(0.01)
    while (y-90 >0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        y = y - 2
        delay(0.01)
    while (30+x < 430):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    for i in range(270,630):
        angle=i*3.14/180
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = r*math.cos(angle)+400
        y = r*math.sin(angle)+300
        delay(0.01)

close_canvas()

