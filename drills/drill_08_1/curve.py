from pico2d import *
import random


open_canvas()
grass = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


def draw_random_soft_move(p1, p2,p3,p4):
    frame = 0
    clip_num =0
    for i in range(0, 100, 5):

        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        if p3[0]-p2[0]>0:
            clip_num = 100
        else:
            clip_num = 0
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        clear_canvas()
        grass.draw(500, 500)
        character.clip_draw(frame * 100,clip_num , 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
        get_events()


size = 20
points =[(random.randint(100, 500), random.randint(50, 500)) for i in range(size)]
n = 1


while True:
    draw_random_soft_move(points[n - 3], points[n - 2], points[n - 1], points[n])
    n = (n + 1) % size


close_canvas()