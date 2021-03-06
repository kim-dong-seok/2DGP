import game_framework
from pico2d import *
from ball import Ball

import game_world

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER =(10.0/0.3)
RUN_SPEED_KMPH =20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        boy.first = get_time()
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS


    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.last = get_time()
        if (boy.last-boy.first) >=10.0 :
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocity, 1)

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:

    @staticmethod
    def enter(boy, event):
        boy.frame = 0
        boy.frame2 = 0
        boy.count = 2.00
        boy.xycount=0.000
        boy.angle = 0
        boy.r = 100
        boy.rx=0
        boy.ry=0
        boy.i=270
        boy.j=630
        boy.opacify=1.00
    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
            if boy.count<=15.00:
                boy.image2.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / boy.count, '', boy.x-15+boy.xycount, boy.y-15+boy.xycount,100, 100)
                boy.image2.opacify(boy.opacify)
                boy.count+=0.01
                boy.xycount+=0.01
            else:
                if boy.i <= 630:
                    boy.angle = boy.i * 3.14 / 180
                    boy.image2.clip_draw(int(boy.frame) * 100, 300, 100, 100, boy.rx, boy.ry)
                    boy.rx = boy.r * math.cos(boy.angle) + boy.x
                    boy.ry = boy.r * math.sin(boy.angle) + boy.y+100
                    boy.i +=  game_framework.frame_time*720
                    boy.image2.opacify(boy.opacify)
        else:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)
            if boy.count<=15.00:
                boy.image2.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / boy.count, '', boy.x+15-boy.xycount, boy.y+15-boy.xycount,100, 100)
                boy.image2.opacify(boy.opacify)
                boy.count+=0.01
                boy.xycount+=0.01
            else:
                if boy.j >= 270:
                    boy.angle = boy.i * 3.14 / 180
                    boy.image2.clip_draw(int(boy.frame) * 100, 200, 100, 100, boy.rx, boy.ry)
                    boy.rx = boy.r * math.cos(boy.angle) + boy.x
                    boy.ry = boy.r * math.sin(boy.angle) + boy.y+100
                    boy.i +=  game_framework.frame_time*720
                    boy.image2.opacify(boy.opacify)
        boy.opacify-=0.01
        if boy.i>=630:
            boy.i=270
        if boy.j >= 270:
            boy.j = 630
        if boy.opacify<=0:
            boy.opacify=1






next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        self.image2 = load_image('animation_sheet.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

