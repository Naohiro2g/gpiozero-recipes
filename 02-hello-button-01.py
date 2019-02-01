from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello!")

button1 = Button(24, pull_up=False)  # means pull_down

button1.when_pressed = say_hello

pause()
