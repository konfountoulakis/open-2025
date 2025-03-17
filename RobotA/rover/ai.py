from microbit import *
from ai_lib import *

rock = False
line = False

def find_rock(ai): 
    ai.switch_function(Ball)
    ai.get_image()
    if ai.get_ball_color == 'Red':
        rock = True
        return rock 
    
    return rock

def find_black_line(ai):
    ai.switch_function(Tracking)
    ai.get_image()
    buff = ai.get_track_data()
    if buff[1] > 100:
        line = True
        return line
    
    return rock