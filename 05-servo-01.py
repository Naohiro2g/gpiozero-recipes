from gpiozero import Servo
from time import sleep

#servo = Servo(17, min_pulse_width=0.55/1000, max_pulse_width=2.65/1000)
servo1 = Servo(17, min_pulse_width=0.58/1000, max_pulse_width=2.70/1000, frame_width=40/1000)

while True:
    servo1.min()
    sleep(1)
#    servo1.mid()
    servo1.value=-0.05
    sleep(1)
    servo1.max()
    sleep(1)
