
from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch
from pyglet.text import Label
from pyglet import clock
import math

def hex_to_rgb(hex_color = None):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16), 255

def check_all_list_same_len(ar = None) :
    template = len(ar[1]) 
    for i in ar :
        if len(i) != template :
            return False
    return True

def num_check_many_list_same_len(ar = None) :
    template = len(ar[1]) 
    for i in ar :
        if len(i) != template :
            return False
    return template

def check_all_num (arr = None) :
    for i in arr :
        if type(i) is not int :
            if type(i) is not float:
                return False
    return True

def num_check_many_list_same_len(ar = None) :
    template = len(ar[1]) 
    for i in ar :
        if len(i) != template :
            return False
    return template

def check_all_list (arr = None) :
    for i in arr :
        if type(i) is not list :
            return False
    return True

def position (arr = None) :

    thick = 80
    in_list = 10
    start = 0
    list_position = []
    if check_all_num(arr) :
        n = len(arr)
        start = (900/2) - ((n*thick) + ((n-1)*in_list))/2
        for i in range(len(arr)) :
            if i != 0 :
                start += thick + in_list
            list_position.append(start)
        return list_position
    else :
        ni = 0
        nj = 0
        for i in range(len(arr)):
            if i != 0 :
                ni += 20
            for j in range(len(arr[i])):
                if j != 0 :
                    nj += 10
        n = len(arr)
        start = (900/2) - ((8*thick) + ni + nj )/2
        for i in range(len(arr)) :
            if i != 0 :
                start += 10
            
            for i2 in range(len(arr[i])):
                if i != 0 or i2 != 0 :
                    start += 90
                
                list_position.append(start)
        list_position = [list_position]
        while len(list_position) != len(arr)  :
            list_position = half(list_position)
        return list_position

def half (arr = None) :

    if check_all_num(arr) :
        position = len(arr) //2
        newarr = [arr[:position],arr[position :]]
        return newarr
    else :
        for i in range(len(arr)) :
            position = len(arr[0])//2
            newarr = [arr[0][:position],arr[0][position :]]
            for i1 in newarr :
                arr.append(i1)
            del arr [0]
        return arr

def all_in_list_zero (position_x = None, original = None) :
    arr = []
    for i1 in range(len(original.copy() )) :
        arr.append(0)
    for i2 in range(len(position_x)//2) :
        arr = half(arr)
    return arr

def all_in_list_zero_merge (position_x = None, original = None) :
    arr = []
    for i1 in range(len(original.copy() )) :
        arr.append(0)
    arr = [arr]
    while len(arr) != len(position_x) :
        arr = half(arr)
    return arr

def only_one (arr = None) :
    for i in range(len(arr)) :
        arr[i] = [arr[i]]
    return arr

def position_merge (arr = None,len_x = None) :
    list = []
    for i in range(len_x) :
        list.append(i)
    list = [list]
    while len(arr) != len(list) :
        list = half(list)
    list_position = []
    arr1 = list.copy()
    if not (check_all_num (arr1)) :
        for i in range(len(arr1)//2) :
            arr1[i].extend(arr1[i+1])
            del arr1[i+1]
        ni = 0
        nj = 0
        for i in range(len(arr1)):
            if i != 0 :
                ni += 20
            for j in range(len(arr1[i])):
                if j != 0 :
                    nj += 10
        start = (900/2) - ((8*80) + ni + nj )/2
        for i in range(len(arr1)) :
            if i != 0 :
                start += 10
            
            for i2 in range(len(arr1[i])):
                if i != 0 or i2 != 0 :
                    start += 90
                
                list_position.append(start)
    else :
        return True
    if check_all_num(list_position) :
        list = []
        for i in list_position :
            list.append([i])
        list_position = list
    
    if len(list) != len(list_position) :
        while len(list) != len(list_position) :
            list_position = merge(list_position)
    return list_position

def merge (arr = None) :

    if check_all_num(arr) :

        return True
    else :
        for i in range(len(arr)//2) :
            arr[i].extend(arr[i+1])
            del arr[i+1]
        return arr

def latest_not_zero (arr = None) :
    if 0 in arr :
        for i in range(len(arr)) :
            if arr[i] != 0 :
                return i
        return 0
    else :
        return 0

def add_num (arr = None) :
    list = []
    for i in range(len(arr)) :
        if arr[i] != 0 :
            list.append(i)
    return list

def check_all_zero (arr) :
    for i in arr :
        if i != 0 :
            return False
    return True

def not_latest_zero (arr = None) :
    if 0 in arr :
        for i in range(len(arr)) :
            if arr[i] == 0 :
                return i
    else :
        return len(arr) + 1
    
def get_all_num (arr = None):
    list = []
    for i in arr :
        if i != 0 :
            list.append(i)
    return list

def everynum_is_zero (arr = None) :
    for i in range (len (arr)) :
        if arr[i] != 0 :
            arr[i] = 0
    return arr

def check_all_list_is_zero (arr) :
    for i in range(len(arr)) :
        for i1 in arr[i] :
            if i1 != 0 :
                return False
    return True

def half_list (arr = None,num = None) :
    list = []
    for i in range(len(arr)) :
        if i == num :
            ar = arr[i]
            list.append(ar[:len(ar)//2])
            list.append(ar[len(ar)//2:])
        else :
            list.append(arr[i])
    return list

def num_check_many_list_same_len(ar) :
    template = len(ar[1]) 
    for i in ar :
        if len(i) != template :
            return False
    return template

class Renderer(Window):
    def __init__(self):
        super().__init__(900, 600, "Merge Sort Visualization")
        self.batch = Batch()
        self.x = [3, 3.5, 6.5, 4, 5, 6, 4.5, 5.5]
        self.position_x = []
        self.or_x = self.x.copy()
        self.len_x = len(self.x)
        self.bars = []
        self.labels = []
        self.start = 0
        self.thick = 80
        self.x1 = []
        self.position_x1 = []
        self.a = 0
        self.b = 0
        self.c = -1
        self.d = 0
        self.e = 0 
        self.f = 0
        self.i = 0
        self.crack_merge = 'crack'
        self.text = 'dont'

        self.labels.append(Label('START', font_name='Arial', font_size=20, x=450  , y=80+35 + 400,color = hex_to_rgb("#FFFFFF"), anchor_x='center', anchor_y='center', batch=self.batch))
        for e, value in enumerate(self.x):
            color = hex_to_rgb("#FFFFFF") 
            self.bars.append(Rectangle(60 + e * 100, 100, 80, value * 50 * 0.75, color=color, batch=self.batch))
            self.labels.append(Label(str(value), font_name='Arial', font_size=15, x=100 + e * 100  , y=80+35,color = hex_to_rgb("#000000"), anchor_x='center', anchor_y='center', batch=self.batch))



    def on_update(self, deltatime):
        self.bars = []
        self.labels = []
        if not ((len(self.x) == 1) and (type(self.x[0]) == list) and (len(self.x[0]) == len(self.or_x))  and self.crack_merge == 'merge' ) and self.text != 'gg' :
            if type(self.x[0]) != int :

                if self.crack_merge == 'crack' and check_all_list_is_zero (self.x) and num_check_many_list_same_len(self.x) == 2 :
                    self.x = self.x1.copy()
                    self.x1 = all_in_list_zero (self.position_x, self.or_x.copy())
                    self.position_x = self.position_x1
                    self.crack_merge = 'merge'
            if self.crack_merge == 'crack' :
                
                if self.a == 0 and self.x == self.or_x :
                    self.position_x = position(self.or_x.copy())
                    for e, value in enumerate(self.or_x.copy()):
                        color = hex_to_rgb("#FFFFFF")
                        self.bars.append(Rectangle(self.position_x[e], 330+10, self.thick, value * 50 * 0.75, color=color, batch=self.batch))
                        self.labels.append(Label(str(value), font_name='Arial', font_size=15, x=self.position_x[e] + 40  , y=340+15,color = hex_to_rgb("#000000"), anchor_x='center', anchor_y='center', batch=self.batch))
                    self.a += 1
                    self.x = half(self.x)
                    self.position_x = half(self.position_x)
                    self.x1 = all_in_list_zero (self.position_x, self.or_x.copy())
                    self.position_x1 = position(self.x1.copy())

                else :
 
                    if self.b < len(self.position_x) :
                        self.x[self.b] , self.x1[self.b] = self.x1[self.b].copy() , self.x[self.b].copy()
                        self.b += 1
                    elif self.b == len(self.position_x) :
                        self.x , self.position_x = self.x1.copy() , self.position_x1
                        self.b = 0
                        self.x1 = all_in_list_zero (self.position_x, self.or_x.copy())

                    for e, value in enumerate(self.x): 
                        for i in range(len(value)): 
                            color =  hex_to_rgb("#FFFFFF")
                            if value[i] != 0:
                                self.bars.append(Rectangle(self.position_x [e][i], 340, self.thick, value[i] * 50 * 0.75, color=color, batch=self.batch))         
                                self.labels.append(Label(str(value[i]), font_name='Arial', font_size=15, x=self.position_x [e][i] + 40  , y=340+15,color = hex_to_rgb("#000000"), anchor_x='center', anchor_y='center', batch=self.batch))
                    for e, value in enumerate(self.x1): 
                        for i in range(len(value)): 
                            color =  hex_to_rgb("#FFFFFF")
                            
                            if value[i] != 0:
                                self.bars.append(Rectangle(self.position_x1 [e][i], 10, self.thick, value[i] * 50 * 0.75, color=color, batch=self.batch))
                                self.labels.append(Label(str(value[i]), font_name='Arial', font_size=15, x=self.position_x1 [e][i] + 40  , y=10+15,color = hex_to_rgb("#000000"), anchor_x='center', anchor_y='center', batch=self.batch))


                    if check_all_list(self.x) and num_check_many_list_same_len(self.x) == 1 and self.b == 0 :
                        self.crack_merge = 'merge'
                    elif self.b == 0 and self.x != only_one(self.or_x.copy()) :
                        self.x = half(self.x)
                        self.position_x = half(self.position_x)
                        self.x1 = all_in_list_zero (self.position_x, self.or_x.copy())
                        self.position_x1 = position(self.position_x.copy())
                        
            elif self.crack_merge == 'merge' :
                if self.c == -1 :
                    self.c += 1
                    for e, value in enumerate(self.x): 
                        for i in range(len(value)): 
                            color =  hex_to_rgb("#FFFFFFF")
                            if value[i] != 0:
                                self.bars.append(Rectangle(self.position_x [e][i], 340, self.thick, value[i] * 50 * 0.75, color=color, batch=self.batch))
                                self.labels.append(Label(str(value[i]), font_name='Arial', font_size=15, x=self.position_x [e][i] + 40  , y=340+15,color = hex_to_rgb("#000000"), anchor_x='center', anchor_y='center', batch=self.batch))
                elif self.c == 0 : 
                    self.position_x1 = position_merge (self.position_x.copy(),self.len_x)
                    self.x1 = (all_in_list_zero_merge (self.position_x.copy(), self.or_x.copy()))
                    self.c += 1
                    self.f = 0
                    self.g = self.x[self.f] + self.x[self.f+1]
                if self.c > 0 :
                    if self.d == 1 :

                        self.x , self.position_x = merge(self.x1.copy()) , merge(self.position_x1.copy())
                        self.x1 = all_in_list_zero_merge (self.position_x.copy(), self.or_x.copy())
                        self.position_x1 = position_merge(self.position_x.copy(),self.len_x)
                        self.d = 0 
                        self.f = 0

                    else :
                        if self.e == 0 :
                            self.check_f0 = [latest_not_zero(self.x[self.f])]
                            self.check_f1 = [latest_not_zero(self.x[self.f+1])]
                            if check_all_zero(self.x[self.f]) :
                                self.check_f1 = add_num(self.x [self.f+1])
                            if check_all_zero(self.x[self.f+1]) :
                                self.check_f0 = add_num(self.x [self.f])
                            self.e += 1
                            self.labels.append(Label(str('check...'), font_name='Arial', font_size=20, x=((self.position_x[self.f][-1]+self.position_x[self.f+1][0]) / 2)+40  , y=320,color = hex_to_rgb("#FFFFFF"), anchor_x='center', anchor_y='center', batch=self.batch))

                        else :
                            self.labels.append(Label(str('move'), font_name='Arial', font_size=20, x=((self.position_x[self.f][-1]+self.position_x[self.f+1][0]) / 2)+40  , y=320,color = hex_to_rgb("#FFFFFF"), anchor_x='center', anchor_y='center', batch=self.batch))
                            self.x1[self.f].extend(self.x1[self.f+1])
                            del self.x1[self.f+1]
                            if not(check_all_zero (self.x[self.f]) or check_all_zero (self.x[self.f+1])) :
                                if self.x[self.f][latest_not_zero(self.x [self.f] )] <= self.x[self.f+1][latest_not_zero(self.x [self.f+1] )] :
         
                                    self.f_move = self.f
                                    self.f_move_position = latest_not_zero(self.x [self.f] )
                                else :
                       
                                    self.f_move = self.f + 1
                                    self.f_move_position = latest_not_zero(self.x [self.f+1] )
                                self.x[self.f_move][self.f_move_position] , self.x1[self.f][not_latest_zero (self.x1[self.f])] = 0 , self.x[self.f_move][self.f_move_position]

                            else :
                      
                                if check_all_zero (self.x[self.f]) :
                                    self.get_list = self.f + 1
                                elif check_all_zero (self.x[self.f+1]) :
                                    self.get_list = self.f
                                self.x1[self.f] = get_all_num (self.x1[self.f])
                                self.list_num_swap = get_all_num(self.x[self.get_list])
                                self.list_num_swap = sorted(self.list_num_swap)

                                for i in self.list_num_swap :
                                    self.x1[self.f].append(i)
                                self.x[self.get_list] = everynum_is_zero(self.x[self.get_list])
                                

                            self.x1 = half_list(self.x1,self.f) #[self.x1[self.f][:len(self.x1[self.f])//2],self.x1[self.f][len(self.x1[self.f])//2:]] #################################

                            self.e = 0
                            self.check_f0 = []
                            self.check_f1 = []

                    if check_all_zero (self.x[self.f]) and check_all_zero (self.x[self.f+1]) :
                        if self.f != (len(self.x) // 2)*2  :
                            self.f+=2
                        if check_all_list_is_zero(self.x) : 
                            self.d = 1 

                    for e, value in enumerate(self.x): 
                        for i in range(len(value)): 
                            color =  hex_to_rgb("#FFFFFFF")
                            if (self.f == e and i in self.check_f0) or (self.f+1 == e and i in self.check_f1) :
                                color =  hex_to_rgb("#00FF00")
                            if value[i] != 0:
                                self.bars.append(Rectangle(self.position_x [e][i], 340, self.thick, value[i] * 50 * 0.75, color=color, batch=self.batch))
                                self.labels.append(Label(str(value[i]), font_name='Arial', font_size=15, x=self.position_x [e][i] + 40  , y=340+15,color = hex_to_rgb("#000000"), anchor_x='center', anchor_y='center', batch=self.batch))
                    if len(self.x1) != len(self.position_x1) :
                        while len(self.x1) != len(self.position_x1) :
                            self.position_x1 = merge(self.position_x1)         
                    for e, value in enumerate(self.x1):
                        for i in range(len(value)): 
                            color =  hex_to_rgb("#FFFFFF")
                            if value[i] != 0:
                                self.bars.append(Rectangle(self.position_x1 [e][i], 10, self.thick, value[i] * 50 * 0.75, color=color, batch=self.batch))
                                self.labels.append(Label(str(value[i]), font_name='Arial', font_size=15, x=self.position_x [e][i] + 40  , y=10+15,color = hex_to_rgb("#000000"), anchor_x='center', anchor_y='center', batch=self.batch))
                    self.c += 1
                


        else :
            self.text = 'gg'
            if self.i == 0 :
                self.x = self.x[0]
                self.i += 1
            self.labels.append(Label('FINISH', font_name='Arial', font_size=20, x=450  , y=80+35 + 400,color = hex_to_rgb("#FFFFFF"), anchor_x='center', anchor_y='center', batch=self.batch))
            for e, value in enumerate(self.x):
                color = hex_to_rgb("#FFFFFF")  # Default color for rectangles
                self.bars.append(Rectangle(60 + e * 100, 100, 80, value * 50 * 0.75, color=color, batch=self.batch))
                self.labels.append(Label(str(value), font_name='Arial', font_size=20, x=100 + e * 100  , y=80+35,color = hex_to_rgb("#000000"), anchor_x='center', anchor_y='center', batch=self.batch))

            clock.unschedule(self.on_update)



    def on_draw(self):
        self.clear()
        self.batch.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 0.5)
run()
