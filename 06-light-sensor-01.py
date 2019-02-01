from gpiozero import LightSensor

ldr1 = LightSensor(11, charge_time_limit=0.001, threshold=0.2)

while True:
    ldr1.wait_for_light()
    print("It's light! :)")
    ldr1.wait_for_dark()
    print("It's dark... :(")
