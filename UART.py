import serial

ser = serial.Serial("COM2",9600)




while True:
    s = str(input())
    ser.write(s.encode())
    if(s=="b"):
        break