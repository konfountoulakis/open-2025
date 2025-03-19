from microbit import *
import random
from nezha import *
from ai import *

        
def stop(nz):
    nz.set_motors(1, 0)
    nz.set_motors(4, 0)
    

def straight(nz, speed): 
    nz.set_motors(1, speed)
    nz.set_motors(4, speed)


def right(nz, speed):
    nz.set_motors(1, 10)
    nz.set_motors(4, speed * 2)   


def left(nz, speed): 
    nz.set_motors(1, speed * 2)
    nz.set_motors(4, 10)
    
def init_servo(nz): 
    nz.set_servo(4, 0)
    
def open(nz): 
    nz.set_servo(4, 90)
def close(nz):
    nz.set_servo(4, 0)

def choose_movement(nz, ai):
    moves = ["straight", "right", "left"]
    move = random.choice(moves)
    if find_black_line(ai):
        straight(nz, -25)
        sleep(1000)
        move = random.choice(move[1:])
    if move == "straight":
        straight(nz, 25)
        sleep(random.randint(1000, 5000))
        stop(nz)
    elif move == "right":
        right(nz, 50)
        sleep(random.randint(1000, 5000))
        stop(nz)
    elif move == "left":
        left(nz, 50)
        sleep(random.randint(1000, 5000))
        stop(nz)
