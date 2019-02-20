# gpiozero-recipes

Sample recipes of [gpiozero](https://gpiozero.readthedocs.io/en/stable/index.html), a simple interface to GPIO devices with Raspberry Pi.

## List of recipes


|Number|File Name|Description|Wiring|Circuit|GPIO|
|:---:|:---|:---|:---:|:---:|:---:|
|1|[01-LED-blinky-01.py](./01-LED-blinky-01.py)|LED blinky.|[<img src="images/01-LED-blinky-01_bb.png" alt="01-LED-blinky-01" title="01-LED-blinky-01" height="50" align="center">](images/01-LED-blinky-01_bb.png)|[-->](images/01-LED-blinky-01_schem.png)|23|
|2|[02-hello-button-01.py](./02-hello-button-01.py)|Push the button<br/> to say hello.|[<img src="images/02-hello-button-01_bb.png" alt="02-hello-button-01" title="02-hello-button-01" height="50" align="center">](images/02-hello-button-01_bb.png)|[-->](images/02-hello-button-01_schem.png)|24|
|3|[03-LED-button-01.py](./03-LED-button-01.py)|Push the button<br/>to turn the LED on.|[<img src="images/03-LED-button-01_bb.png" alt="03-LED-button-01" title="03-LED-button-01" height="50" align="center">](images/03-LED-button-01_bb.png)|[-->](images/03-LED-button-01_schem.png)|23,24|
|Number|File Name|Description|Wiring|Circuit|GPIO|



- [04-PWM-LED-01.py](./04-PWM-LED-01.py)
[--> wiring <img src="images/04-PWM-LED-01_bb.png" alt="04-PWM-LED-01" title="04-PWM-LED-01" height="50" align="center">](images/04-PWM-LED-01_bb.png)
[--> circuit](images/04-PWM-LED-01_schem.png)

LED brightness control with PWM, or Pulse Witdh Modulation.

- [05-servo-01.py](./05-servo-01.py)
[--> wiring <img src="images/05-servo-01_bb.png" alt="05-servo-01" title="05-servo-01" height="50" align="center">](images/05-servo-01_bb.png)
[--> circuit](images/05-servo-01_schem.png)

Turn the servo moter.

- [06-light-sensor-01.py](./06-light-sensor-01.py)
[--> wiring <img src="images/06-light-sensor-01_bb.png" alt="06-light-sensor-01" title="06-light-sensor-01" height="50" align="center">](images/06-light-sensor-01_bb.png)
[--> circuit](images/06-light-sensor-01_schem.png)

Say when it's light or dark.

- [07-distance-sensor-01.py](./07-distance-sensor-01.py)
[--> wiring <img src="images/07-distance-sensor-01_bb.png" alt="07-distance-sensor-01" title="07-distance-sensor-01" height="50" align="center">](images/07-distance-sensor-01_bb.png)
[--> circuit](images/07-distance-sensor-01_schem.png)

Supersonic distance sensor HC-SR04. Trig=GPIO23, Echo=GPIO24

- [07-distance-sensor-02.py](./07-distance-sensor-02.py)
[--> wiring <img src="images/07-distance-sensor-02_bb.png" alt="07-distance-sensor-02" title="07-distance-sensor-02" height="50" align="center">](images/07-distance-sensor-02_bb.png)
[--> circuit](images/07-distance-sensor-02_schem.png)

Supersonic distance sensor and 4-digit 7-segment LED display.

- [08-motion-sensor-01.py](./08-motion-sensor-01.py)
[--> wiring <img src="images/08-motion-sensor-01_bb.png" alt="08-motion-sensor-01" title="08-motion-sensor-01" height="50" align="center">](images/08-motion-sensor-01_bb.png)
[--> circuit](images/08-motion-sensor-01_schem.png)

PIR (Passive Infrared Ray) motion sensor.


## How to eat, or run the code

1. Clone the code down to you computer.
2. Go into the working directory.
3. Make the circuits with circuit diagrams made with [Fritzing](http://fritzing.org/home/).
4. Run the code by Python.
5. Enjoy coding, hacking, and tinkering!

```
$ cd Documents
$ cd Python\ Projects
$ git clone paste-the-URL-from-the-green-button-of-Clone-or-download
$ cd gpiozero-recipes
$ python3 01-LED-blinky.py
```
