from microbit import *
import random
from nezha import *

def choose_movement(nz, speed):
    moves = ["straight", "right", "left"]
    move = random.choice(moves)
    if move == "straight":
        straight_distance(nz, speed, random.randint(1, 10))
    elif move == "right":
        right_deg(nz, speed, random.randint(1, 180))
    elif move == "left":
        left_deg(nz, speed, random.randint(1, 180))

def calc_distnce(distance, speed):
    return distance*80/100

def straight(nz, speed): 
    nz.set_motors(1, speed)
    nz.set_motors(2, speed)

def straight_distance(nz, speed, distance):
    straight(nz, speed)
    sleep(calc_distnce(distance, speed))
    straight(nz, 0)

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

