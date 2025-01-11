from microbit import *
import radio 
radio.config(group = 2)
radio.on()

sensors = ['T', 'U', 'D', 'L', 'C']

uart.init(115200)

def decrypt(messagge): pass

def warn(sensor, value): pass

while True:
    message = radio.receive()
    if message and message[0] in sensors:
        display.scroll(message)
        uart.write(message)
        sensor, value = message[0], decrypt(message)
        warn(sensor, value)

