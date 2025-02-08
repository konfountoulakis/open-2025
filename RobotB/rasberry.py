#!/usr/bin/env python
import time
import serial
from datetime import datetime
from csv import writer
import http.server

ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

# need to chane that based on the data we get from the microbit
while True:
    data=ser.readline()
    if data:
        dt = datetime.now()
        datestamp = str(dt)[:16]
        newData = [datestamp,0,0,0,0,0]
        newData[data[0]]=data[1:] #data0 einai h thesh kai to data[1:] enai ta stoixeia
        print(newData)
        with open('data.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(newData)
            f_object.close()
