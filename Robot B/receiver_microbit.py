from microbit import *

pot_value = 0
pot_prev = 0
data_in = ''

while True:
    sleep(100)
    
    # Read analog value and send serial uart data to Raspberry Pi
    adc_pot = pin2.read_analog()
    pot_value = int(adc_pot / 125)
    if pot_value != pot_prev:
        print(pot_value)
        pot_prev = pot_value

