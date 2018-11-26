import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0,1600 ),random.randint(0,1200), 0

    def set_center_object(self, boy):
        self.center_object = boy
    
    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(1600-self.window_left, 1200-self.window_bottom)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.window_left = clamp(0,
                                 int(self.center_object.x) - self.canvas_width//2,
                                 self.x - self.canvas_width)
        self.window_bottom = clamp(0,
                                   int(self.center_object.y) - self.canvas_height//2,
                                   self.y - self.canvas_height)

