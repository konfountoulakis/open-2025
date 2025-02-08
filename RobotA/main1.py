# Imports go at the top
from microbit import *
import movements as mv 

wk = WUKONG()
wk.set_motors(1,50)
wk.set_motors(2,50)

# Code in a 'while True:' loop repeats forever
while True:
    mv.straiht(wk, 50)
    mv.sleep(5000)
    mv.right(wk, 50)
    sleep(5000)
    left(wk, 50)
    sleep(5000)
    init_servo(wk , 1 , 90) 
    init_servo(wk, 2, 90)
    rotate(wk, 90)
    sleep(5000)
    
    down(wk)
    sleep(5000)
    up(wk)
    sleep(5000)
    open(wk)
    sleep(5000)
    close(wk)
    sleep(5000)
    grab_leave(wk, 90)
    sleep(5000)
    
