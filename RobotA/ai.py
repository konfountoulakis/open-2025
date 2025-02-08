from movements import *
from microbit import *
from ai_lib import *

rock = False

def find_rock(ai): 
    ai.get_image()
    if ai.get_ball_color == 'Red':
        rock = True  

def rock_pos(ai, wk): 
    ai.get_image()
    x, y = ai.get_ball_data()[0], ai.get_ball_data()[1]

# needs to be tested maybe we can have a curve as the correct position
def check_pos(ai):
    ai.get_image()
    x, y = ai.get_ball_data()[0], ai.get_ball_data()[1]
    if x < 2.5 and x > 1.5 and y < 2.5 and y > 1.5:
        return 'center'
    else: 
        return 'not center'

  
    

