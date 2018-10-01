from pico2d import *
import turtle
import random



open_canvas()
grass = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


def draw_line(p1, p2):
    frame = 0
    clip_num =0
    for i in range(0, 100 + 1, 5):

        t = i / 100
        x = (1-t)*p1[0]+t*p2[0]
        if p2[0]-p1[0]>0:
            clip_num = 100
        else:
            clip_num = 0
        y = (1 - t) * p1[1] + t * p2[1]
        clear_canvas()
        grass.draw(500, 500)
        character.clip_draw(frame * 100,clip_num , 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
        get_events()

size = 20
points =[(random.randint(0, 500), random.randint(0, 500)) for i in range(size)]
n = 1


while True:
    draw_line(points[n-1], points[n])
    n = (n+1) % size


close_canvas()