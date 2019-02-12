from gpiozero import DistanceSensor
from time import sleep
from decimal import Decimal, ROUND_HALF_UP
import sys

import tm1637

display = tm1637.TM1637(CLK=20, DIO=21, brightness=7)
display.Clear()

sensor = DistanceSensor(echo=24, trigger=23)


print('Display distance in mm on the 4-digit 7-segment LED.')
print('Be sure to supply 3.3V (not 5V) to the LED module.')
print('OK to supply 5V to the Supersonic Distance Sensor but you need dividing resistors to receive Echo.')
print('GPIO connection:\n\tSupersonic Distance Senser (Trigger=23, Echo=24)\n\tLED Module (CLK=20, DIO=21)\n\n\n')


while True:
    distance_mm = sensor.distance * 1000 #  make it in mm
    distance = Decimal(str(distance_mm)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    print('Distance to nearest object is', distance, 'mm')

    data = [0,0,0,0]
    if distance_mm >= 1000:
        data = [14,14,14,14]  # EEEE: out of range
    else:
        data[0] = 0
        data[1] = int(distance_mm//100)
        data[2] = int((distance_mm%100-distance_mm%10)//10)
        data[3] = int(float(distance)%10)    #  ROUND_HALF_UP
#    print('LED Module (', data[0], data[1], data[2], data[3], ')')
#    print('(', distance_mm, ')')
    display.Show(data)
#    sleep(1)
    sleep(0.25)
