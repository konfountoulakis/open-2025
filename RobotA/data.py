from microbit import *
import radio

def avg(values): 
    total = sum(values)
    count = len(values)
    average = total / count
    return average

def change(value):
    x = ((value*100)/1023)
    return x 
    
def encrypt(sensor, value):
    mes = sensor + str(value)
    return mes
    
    
def collect_send(sensor, pin):
    values= []
    for i in range(10):
        values.append(pin.read_analog())
        sleep(100)
    average = change(avg(values))
    mes= encrypt(sensor,average) 
    radio.send(mes)

    
    change(value):
    x = ((value))
