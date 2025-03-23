# Imports go at the top
from microbit import *
from data import *
import radio 
radio.config(group = 2)
radio.on()

pairs = {'T': temperature(), 'U': pin0.read_analog(), 'D': pin1.read_analog(), 'L':display.read_light_level(), 'C':pin2.read_analog()}
sensors = list(pairs.keys())

# Code in a 'while True:' loop repeats forever
while True:
    for i in range(len(sensors)):
        display.scroll(sensors[i]+ str(pairs[sensors[i]]))
        collect_send(sensors[i], pairs[sensors[i]])
