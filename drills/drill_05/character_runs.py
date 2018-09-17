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
            delay(0.05)
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
            delay(0.05)
            get_events()


while True:

    #1
    move_character(203, 535, 132, 243)
    #2
    move_character(132, 243, 535, 470)
    #3
    move_character(535, 470, 477, 203)
    #4
    move_character(477, 203, 715, 136)
    #5
    move_character(715, 136, 316, 225)
    #6
    move_character(316, 225, 510, 92)
    #7
    move_character(510, 92, 692, 518)
    #8
    move_character(692, 518, 682, 336)
    #9
    move_character(682, 336, 712, 349)
    #10
    move_character(712, 349, 203, 535)

close_canvas()