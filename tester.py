import serial
import sys,os


ser = serial.Serial(port='COM3', baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=5)
try:
    ser.isOpen()
    print("Serial port is open")
except:
    print('Error opening')
    
    exit()

value = []

if(ser.isOpen()):
    try:
        while True:
            data = ser.read()
            text = data.decode("utf-8")
            if text != ".":
                value.append(text)
            if text == ".":
                hor = "".join(value)
                print(hor)
                value.clear()

    except Exception:
        print('Error exception')
else:
    print('Cannot open serial port')