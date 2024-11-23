# RaspberryPi3-Motor-Measurer
Moves a motor in one direction if there is an object is near (closer than 30 cm) or in a different one if not. The measures are conducted via an ultrasonic measurer which sends a sound from a speaker and gets it from a microphone; The code calculates the distance based on how long it took the sound to reach the microphone.

![](/image-previewpng)

## Hardware

- Platform: `Raspberry Pi 3 B+`
- Ultrasonic distance measurer: `HC-SRO4`
- Step motor: `SBT0811`

## Usage
Clone the code

`https://github.com/Resadesker/RaspberryPi3-Motor-Measurer.git`

**Connect pins:**

Vcc, Gnd for motor and distance meter. GPIOs:

Distance meter: 
```
TRIG - 14
ECO - 15
```

Motor:
```
PIN1 - 12
PIN2 - 16
PIN3 - 20
PIN4 - 21
```

Install libraries

`
pip install RPi.GPIO
`

Launch

```
cd RaspberryPi3-Motor-Measurer/
python main.py
```
