from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global  m_x, m_y
    global x,y
    global dir
    events= get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            m_x, m_y = event.x, KPU_HEIGHT -1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
m_x, m_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir=0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw(m_x,m_y)

    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    if dir != 0:
        frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()




