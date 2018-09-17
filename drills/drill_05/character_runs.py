from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_character(start_x , start_y, last_x, last_y):
    frame = 0
    x = start_x
    y = start_y
    if start_x > last_x:
        while x > last_x:
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x -= (start_x-last_x)//10
            y -= (start_y-last_y)//10
            delay(0.5)
            get_events()
    elif start_x <= last_x:
        while x <= last_x:
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x -= (start_x-last_x)//10
            y -= (start_y-last_y)//10
            delay(0.5)
            get_events()


while True:
    
    #1
    move_character(203, 535, 132, 243)


close_canvas()