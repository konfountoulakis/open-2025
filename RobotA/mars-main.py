# Imports go at the top
from microbit import *
from ai_lib import *
from wukong import *
from ai import *
from data import *
from movements import *
import radio

# Init of componets
wk = WUKONG()
ai = AILENS()
ai.switch_function(Learn)

# Init radio
radio.config(group = 2)
radio.on()

max_rocks = 3
num_rocks = 0

# move randomly until the rock is found maybe we need to create a custom random function to make sure 
# the robot is not going back and forth and is looking in new places
# we also need to keep track of how many rocks we have to return to the base once we have found them all
# i think we will be checking the enviromental data every 5 seconds without moving
# if there is a lot of dust we have to do something to keep our solar panels clean maybe go back to base

# if we found the correct rock we will move accordingly until we have checket the position is corerect
# and then we will grab the rock and return to base if we have found all the rocks