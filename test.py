import serial
import sys,os

# List of pathnames
fileNames = ['data/3v.txt', 'data/4,5v.txt', 'data/6v.txt',
             'data/7,5v.txt', 'data/9v.txt', 'data/12v.txt']

# Establish serial communications
ser = serial.Serial(port='COM3', baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=2)

# Assert serial connection is availible
assert ser.isOpen()

if(ser.isOpen()):
    try:
        while True:
            # Read data
            data = ser.read()
            print(data)
            # Write data to textfile
            with open(fileNames[0], "a") as myfile:
                myfile.write(str(data) + '\n')
    # Catch error
    except Exception:
        print('Error exception')
else:
    print('Cannot open serial port')
