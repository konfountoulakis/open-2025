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

# Init radio
radio.config(group = 2)
radio.on()

