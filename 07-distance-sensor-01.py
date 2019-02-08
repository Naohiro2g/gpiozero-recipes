from gpiozero import DistanceSensor
from time import sleep
from decimal import Decimal, ROUND_HALF_UP
import sys

sensor = DistanceSensor(echo=24, trigger=23)

print('trigger is configured to',sensor.trigger)
print('echo is configured to',sensor.echo)

#    sys.exit()

while True:
#    print('Distance to nearest object is', sensor.distance * 100, 'cm')
#    print('Distance to nearest object is', '{:.2f}'.format(sensor.distance * 100), 'cm')

    distance = Decimal(str(sensor.distance * 100)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    print('Distance to nearest object is', distance, 'cm')
    sleep(1)
