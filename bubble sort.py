import pyglet
from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch
from pyglet.text import Label
from pyglet import clock

def hex_to_rgb(hex_color):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16), 255

class Renderer(Window):
    def __init__(self):
        super().__init__(900, 600, "Bubble Sort Visualization")
        self.batch = Batch()
        self.x = [3, 3.5, 6.5, 4, 5, 6, 4.5, 5.5]
        self.bars = []
        self.labels = []
        self.i = 0
        self.j = 0
        self.k = 0
        self.n = len(self.x)
        self.labels.append(Label('START', font_name='Arial', font_size=20, x=450  , y=80+35 + 400,color = hex_to_rgb("#FFFFFF"), anchor_x='center', anchor_y='center', batch=self.batch))
        for e, value in enumerate(self.x):
            color = hex_to_rgb("#FFFFFF")  # Default color for rectangles
            self.bars.append(Rectangle(60 + e * 100, 100, 80, value * 50 * 0.75, color=color, batch=self.batch))
            self.labels.append(Label(str(value), font_name='Arial', font_size=15, x=100 + e * 100  , y=80+35,color = hex_to_rgb("#000000"), anchor_x='center', anchor_y='center', batch=self.batch))

    def on_update(self, deltatime):
        n = len(self.x)
        if self.i < n - 1:
            if self.j < n - self.i -1 :
                self.bars = []
                self.labels = []

                if self.k == 0 :
                    self.labels.append(Label('checking ...', font_name='Arial', font_size=20, x=self.j*100 +60 +87.5, y=80, anchor_x='center', anchor_y='center', batch=self.batch))
                    for e, value in enumerate(self.x):
                        if e == self.j or e == self.j + 1 :
                            color = hex_to_rgb("#00FF00") 
                        else :
                            color = hex_to_rgb("#FFFFFF")
                        self.bars.append(Rectangle(60 + e * 100, 100, 80, value * 50 * 0.75, color=color, batch=self.batch)) 
                        self.labels.append(Label(str(value), font_name='Arial', font_size=15, x=100 + e * 100  , y=80+35,color = hex_to_rgb("#000000"), anchor_x='center', anchor_y='center', batch=self.batch))  
                    self.k = 1

                elif self.k == 1 :
                    if self.x[self.j] > self.x[self.j + 1]:
                        self.x[self.j], self.x[self.j + 1] = self.x[self.j + 1], self.x[self.j]
                        swap_text = "Swap"
                    else:
                        swap_text = "No Swap"
                    self.labels.append(Label(swap_text, font_name='Arial', font_size=20, x=self.j*100 +60 +87.5, y=80, anchor_x='center', anchor_y='center', batch=self.batch))
                    for e, value in enumerate(self.x):
                        if e == self.j or e == self.j + 1 :
                            color = hex_to_rgb("#00FF00") 
                        else :
                            color = hex_to_rgb("#FFFFFF")
                        self.bars.append(Rectangle(60 + e * 100, 100, 80, value * 50 * 0.75, color=color, batch=self.batch))   
                        self.labels.append(Label(str(value), font_name='Arial', font_size=15, x=100 + e * 100  , y=80+35,color = hex_to_rgb("#000000"), anchor_x='center', anchor_y='center', batch=self.batch))
                    self.k = 0
                
                if self.k == 0 :
                    self.j += 1
            else:
                self.i += 1
                self.j = 0
        elif self.i == n - 1:
            self.bars = []
            self.labels = []
            color = hex_to_rgb("#FFFFFF")
            for e, value in enumerate(self.x):
                self.bars.append(Rectangle(60 + e * 100, 100, 80, value * 50 * 0.75, color=color, batch=self.batch))   
                self.labels.append(Label(str(value), font_name='Arial', font_size=15, x=100 + e * 100  , y=80+35,color = hex_to_rgb("#000000"), anchor_x='center', anchor_y='center', batch=self.batch))
                self.labels.append(Label('FINISH', font_name='Arial', font_size=20, x=450  , y=80+35 + 400,color = hex_to_rgb("#FFFFFF"), anchor_x='center', anchor_y='center', batch=self.batch))
            clock.unschedule(self.on_update)



    def on_draw(self):
        self.clear()
        self.batch.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 0.5)
run()