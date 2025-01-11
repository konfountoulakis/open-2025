from wukong import *

# όλες οι τιμές πρέπει να αλλαχθούν
def straiht(wk, speed): 
    wk.set_motors(1, speed)
    wk.set_motors(2, speed)

def right(wk, speed): 
    wk.set_motors(1, speed)
    wk.set_motors(2, speed / 2)
def left (wk, speed): 
    wk.set_motors(1, speed)
    wk.set_motors(2, speed / 2)
    
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

