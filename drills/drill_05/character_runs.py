from pico2d import *
open_canvas()
grass = load_image('grass.png')

character = load_image('animation_sheet.png')






def move_character_01():
    x = 203
    y = 535
    frame = 0
    while x>132:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= (203-132)//20
        y -= (535-243)//20
        delay(0.1)
        get_events()
def move_character_02():
    x = 132
    y = 243
    frame = 0
    while x<535:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += (535-132)//20
        y += (470-243)//20
        delay(0.1)
        get_events()
def move_character_03():
    x = 535
    y = 470
    frame = 0
    while x>477:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= (535-477)//20
        y -= (470-203)//20
        delay(0.1)
        get_events()
def move_character_04():
    x = 477
    y = 203
    frame = 0
    while x<715:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += (715-535)//20
        y -= (203-136)//20
        delay(0.1)
        get_events()
        
#move_character_01()
#move_character_02()
#move_character_03()
#move_character_04()

close_canvas()