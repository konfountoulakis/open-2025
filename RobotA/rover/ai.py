from movements import *
from microbit import *
from ai_lib import *

rock = False

def find_rock(ai): 
    ai.get_image()
    if ai.get_ball_color == 'Red':
        rock = True
        return rock 