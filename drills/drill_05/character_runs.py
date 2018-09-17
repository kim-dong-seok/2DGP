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
        x -= (203-132)//15
        y -= (535-243)//15
        delay(0.1)
        get_events()



move_character_01()



close_canvas()