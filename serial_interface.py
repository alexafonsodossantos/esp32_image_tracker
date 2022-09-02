import serial
 


def send_pos(pos):
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = '/dev/ttyUSB0'
    ser.open()
    values = bytearray([])
    values.append(pos)
    ser.write(values)
    ser.close()
