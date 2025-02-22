# Imports go at the top
from microbit import *
from data import *
import radio 
radio.config(group = 2)
radio.on()

pairs = {'T': pin0, 'U': pin1, 'D': pin2, 'L':pin3, 'C':pin4}
sensors = list(pairs.keys())

# Code in a 'while True:' loop repeats forever
while True:
    for i in range(len(sensors)):
        collect_send(sensors[i], pairs[sensors[i]])
