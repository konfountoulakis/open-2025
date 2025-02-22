# Imports go at the top
from microbit import *
import radio 
radio.config(group = 2)
radio.on()

sensors = ['T', 'U', 'D', 'L', 'C']

uart.init(115200)

def decrypt(message): 
    return message[1:]

def warn(sensor, value): pass

while True:
    message = radio.receive()
    if message and message[0] in sensors:
        display.scroll(message)
        pos=sensors.index(message[0])
        new_message=str(pos+1)+decrypt(message)
        uart.write(new_message)
        sensor, value = message[0], decrypt(message)
        
