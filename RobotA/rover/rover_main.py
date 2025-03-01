from microbit import *
from movements import *
from ai import *
import radio 
radio.config(group = 2)
radio.on()

nz = NEZHA()
init_servo(nz, 1, 90)
init_servo(nz, 2, 90)
init_servo(nz, 3, 90)
init_servo(nz, 4, 90)

max_rocks = 4

while True:
    while max_rocks < 4:
        message = radio.receive()
        if find_rock():
            if check_pos() == 'center':
                straight_distance(nz, 100, 10)
                grab_leave(nz, 180)
        choose_movement(nz, 50)
        if message:
            if message[0] == "D":
                right(nz, 100)
                sleep(500)
                straight(0)
        

