from gpiozero import PWMLED
from time import sleep

led1 = PWMLED(23)

while True:
    led1.value = 0  # off
    sleep(0.5)
    led1.value = 0.2
    sleep(0.5)
    led1.value = 0.4
    sleep(0.5)
    led1.value = 0.8
    sleep(0.5)
    led1.value = 1  # full brightness
    sleep(1)
