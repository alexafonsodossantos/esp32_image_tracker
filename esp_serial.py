from serial_interface import *



window_w = 640
window_c = window_w / 2
x = 240


servo_pos = int((180 / window_w ) * x)

print(servo_pos)

send_pos(servo_pos)