from microbit import *
import random
from nezha import *
from ai import *

        
def stop(nz):
    nz.set_motors(1, 0)
    nz.set_motors(4, 0)
    
def calc_distnce(distance):
    return distance*80/100

def straight(nz, speed): 
    nz.set_motors(1, speed)
    nz.set_motors(4, speed)

def straight_distance(nz, speed, distance):
    straight(nz, speed)
    sleep(calc_distnce(distance))
    stop(nz)

def calc_deg(deg):
    return deg*10/90

def right(nz, speed):
    nz.set_motors(1, speed / 2)
    nz.set_motors(4, speed)   

def right_deg(nz, speed, deg): 
    nz.set_motors(1, speed / 2)
    nz.set_motors(4, speed)
    sleep(calc_deg(deg))
    stop(nz)

def left_deg(nz, speed, deg): 
    nz.set_motors(1, speed)
    nz.set_motors(4, speed / 2)
    sleep(calc_deg(deg))
    stop(nz)
    
def init_servo(nz): 
    nz.set_servo(4, 90)
    
def open(nz): 
    nz.set_servo(4, 90)
def close(nz):
    nz.set_servo(4, 180)

def choose_movement(nz, ai, speed):
    moves = ["straight", "right", "left"]
    move = random.choice(moves)
    if find_black_line(ai):
        straight_distance(nz, -25, 50)
        move = random.choice(move[1:])
    if move == "straight":
        straight_distance(nz, speed, random.randint(1, 10))
    elif move == "right":
        right_deg(nz, speed, random.randint(1, 180))
    elif move == "left":
        left_deg(nz, speed, random.randint(1, 180))

