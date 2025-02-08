from microbit import *
from wukong import *

# if i put sleep one what distance will i i do, know take the distance and give the time i need to reach it
def calc_distnce(distance, speed):
    return 0

# όλες οι τιμές πρέπει να αλλαχθούν
def straight(wk, speed): 
    wk.set_motors(1, speed)
    wk.set_motors(2, speed)

def straight_distance(wk, speed, distance):
    straight(wk, speed)
    sleep(calc_distnce(distance, speed))
    straight(wk, 0)

# we will find the math we need to go from degrees to time
def calc_deg(deg, speed):
    return 0

def right_deg(wk, speed, deg): 
    wk.set_motors(1, speed)
    wk.set_motors(2, speed / 2)
    sleep(calc_deg(deg, speed))
    wk.set_motors(1, 0)
    wk.set_motors(2, 0)

def left_deg(wk, speed, deg): 
    wk.set_motors(1, speed)
    wk.set_motors(2, speed / 2)
    sleep(calc_deg(deg))
    wk.set_motors(1, 0)
    wk.set_motors(2, 0)

    
def init_servo(wk, servo, deg): 
    wk.set_servo(servo, 90)
    
def rotate(wk, deg): 
    wk.set_servo(1, deg)
    
def down(wk):
    wk.set_servo(2, 90)
def up(wk): 
    wk.set_servo(2, 180)
    
def open(wk): 
    wk.set_servo(3, 90)
def close(wk):
    wk.set_servo(3, 180)
    
def grab_leave(wk, deg): 
    rotate(wk, deg)
    down(wk)
    open(wk)
    close(wk)
    up(wk)

