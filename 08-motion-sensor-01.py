from gpiozero import MotionSensor, LED
from signal import pause
import datetime

# pir: pyroelectric infrared switch

pir1 = MotionSensor(4)
led1 = LED(23)

def found():
    led1.on()
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), " detected!")
    return

def lost():
    led1.off()
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), " lost...\n")
    return

pir1.when_motion = found
pir1.when_no_motion = lost

pause()
