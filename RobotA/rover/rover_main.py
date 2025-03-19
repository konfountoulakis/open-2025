from microbit import *
from movements import *
from ai import *
import radio 
radio.config(group = 2)
radio.on()

ai = AILENS()
nz = NEZHA()

ai.switch_function(Ball)
init_servo(nz)

max_rocks = 4

while True:
    while max_rocks < 4:
        message = radio.receive()
        if find_rock(ai):
            open(nz)
            straight(nz, 20)
            sleep(500)
            stop(nz)
            close(nz)
        choose_movement(nz, 50)
        if message:
            if message[0] == "D":
                right(nz, 50)
                sleep(500)
                stop(nz)
    
