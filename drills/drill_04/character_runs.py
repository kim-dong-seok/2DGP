from pico2d import *
open_canvas()
grass = load_image('grass.png')

character = load_image('animation_sheet.png')
x =0
y=0
frame=0
while (True):
    if x>=800:
        y=0
    elif x<=0:
        y=1


    if y==0:
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame * 100,0,100,100,x,90)
        update_canvas()
        frame=(frame+1)%8
        x=x-10
        delay(0.05)
        get_events()
    elif y==1:
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame * 100,100,100,100,x,90)
        update_canvas()
        frame=(frame+1)%8
        x=x+10
        delay(0.05)
        get_events()

close_canvas()

