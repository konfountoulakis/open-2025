from microbit import *
from nezha import *

# if i put sleep one what distance will i i do, know take the distance and give the time i need to reach it
def calc_distnce(distance, speed):
    return distance*80/100

# όλες οι τιμές πρέπει να αλλαχθούν
def straight(nz, speed): 
    nz.set_motors(1, speed)
    nz.set_motors(2, speed)

def straight_distance(nz, speed, distance):
    straight(nz, speed)
    sleep(calc_distnce(distance, speed))
    straight(nz, 0)

# we will find the math we need to go from degrees to time
def calc_deg(deg, speed):
    return deg*10/90

def right_deg(nz, speed, deg): 
    nz.set_motors(1, speed)
    nz.set_motors(2, speed / 2)
    sleep(calc_deg(deg, speed))
    nz.set_motors(1, 0)
    nz.set_motors(2, 0)

def left_deg(nz, speed, deg): 
    nz.set_motors(1, speed)
    nz.set_motors(2, speed / 2)
    sleep(calc_deg(deg))
    nz.set_motors(1, 0)
    nz.set_motors(2, 0)

    
def init_servo(nz, servo, deg): 
    nz.set_servo(servo, 90)
    
def rotate(nz, deg): 
    nz.set_servo(1, deg)
    
def down(nz):
    nz.set_servo(2, 90)
def up(nz): 
    nz.set_servo(2, 180)
    
def open(nz): 
    nz.set_servo(3, 90)
def close(nz):
    nz.set_servo(3, 180)
    
def grab_leave(nz, deg): 
    rotate(nz, deg)
    down(nz)
    open(nz)
    close(nz)
    up(nz)

