# gpiozero-recipes

Sample recipes of [gpiozero](https://gpiozero.readthedocs.io/en/stable/index.html), a simple interface to GPIO devices with Raspberry Pi.

## List of recipes


|Number|File Name|Description|Wiring|Circuit|GPIO|
|:---:|:---|:---|:---:|:---:|:---:|
|1|[01-LED-blinky-01.py](./01-LED-blinky-01.py)|LED blinky.|[<img src="images/01-LED-blinky-01_bb.png" alt="01-LED-blinky-01" title="01-LED-blinky-01" height="50" align="center">](images/01-LED-blinky-01_bb.png)|[-->](images/01-LED-blinky-01_schem.png)|23|
|2|[02-hello-button-01.py](./02-hello-button-01.py)|Push the button<br/> to say hello.|[<img src="images/02-hello-button-01_bb.png" alt="02-hello-button-01" title="02-hello-button-01" height="50" align="center">](images/02-hello-button-01_bb.png)|[-->](images/02-hello-button-01_schem.png)|24|
|3|[03-LED-button-01.py](./03-LED-button-01.py)|Push the button<br/>to turn the LED on.|[<img src="images/03-LED-button-01_bb.png" alt="03-LED-button-01" title="03-LED-button-01" height="50" align="center">](images/03-LED-button-01_bb.png)|[-->](images/03-LED-button-01_schem.png)|23,24|
|4|[04-PWM-LED-01.py](./04-PWM-LED-01.py)|LED brightness control with PWM, or Pulse Witdh Modulation.|[<img src="images/04-PWM-LED-01_bb.png" alt="04-PWM-LED-01" title="04-PWM-LED-01" height="50" align="center">](images/04-PWM-LED-01_bb.png)|[-->](images/04-PWM-LED-01_schem.png)|23|
|5|[05-servo-01.py](./05-servo-01.py)|Turn the servo moter.|[<img src="images/05-servo-01_bb.png" alt="05-servo-01" title="05-servo-01" height="50" align="center">](images/05-servo-01_bb.png)|[-->](images/05-servo-01_schem.png)|17|
|6|[06-light-sensor-01.py](./06-light-sensor-01.py)|Say when it's light or dark.|[<img src="images/06-light-sensor-01_bb.png" alt="06-light-sensor-01" title="06-light-sensor-01" height="50" align="center">](images/06-light-sensor-01_bb.png)|[-->](images/06-light-sensor-01_schem.png)|11|
|7|[07-distance-sensor-01.py](./07-distance-sensor-01.py)|Supersonic distance sensor.|[<img src="images/07-distance-sensor-01_bb.png" alt="07-distance-sensor-01" title="07-distance-sensor-01" height="50" align="center">](images/07-distance-sensor-01_bb.png)|[-->](images/07-distance-sensor-01_schem.png)|23,24|
|8|[07-distance-sensor-02.py](./07-distance-sensor-02.py)|Supersonic distance sensor and 4-digit 7-segment LED display.|[<img src="images/07-distance-sensor-02_bb.png" alt="07-distance-sensor-02" title="07-distance-sensor-02" height="50" align="center">](images/07-distance-sensor-02_bb.png)|[-->](images/07-distance-sensor-02_schem.png)|20,21,23,24|
|9|[08-motion-sensor-01.py](./08-motion-sensor-01.py)|PIR (Passive Infrared Ray) motion sensor.|[<img src="images/07-distance-sensor-02_bb.png" alt="07-distance-sensor-02" title="07-distance-sensor-02" height="50" align="center">](images/07-distance-sensor-02_bb.png)|[-->](images/08-motion-sensor-01_schem.png)|4|
|Number|File Name|Description|Wiring|Circuit|GPIO|



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
