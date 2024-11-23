import RPi.GPIO as GPIO
import time

# Define GPIO pins
TRIG = 14
ECHO = 15

PIN1 = 12
PIN2 = 16
PIN3 = 20
PIN4 = 21

dist = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10 microseconds pulse
    GPIO.output(TRIG, False)

    # Wait for the echo to start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # Wait for the echo to end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # in cm
    distance = round(distance, 2)
    
    return distance

def spin():
    if (dist > 30):
        GPIO.output(PIN1, True)
        time.sleep(0.005)
        GPIO.output(PIN1, False)
        GPIO.output(PIN2, True)
        time.sleep(0.005)
        GPIO.output(PIN2, False)
        GPIO.output(PIN3, True)
        time.sleep(0.005)
        GPIO.output(PIN3, False)
        GPIO.output(PIN4, True)
        time.sleep(0.005)
        GPIO.output(PIN4, False)
    else:
        GPIO.output(PIN4, True)
        time.sleep(0.005)
        GPIO.output(PIN4, False)
        GPIO.output(PIN3, True)
        time.sleep(0.005)
        GPIO.output(PIN3, False)
        GPIO.output(PIN2, True)
        time.sleep(0.005)
        GPIO.output(PIN2, False)
        GPIO.output(PIN1, True)
        time.sleep(0.005)
        GPIO.output(PIN1, False)

try:
    while True:
        dist = measure_distance()
        spin()
        print(f"Distance: {dist} cm")
        time.sleep(0.005)
except KeyboardInterrupt:
    print("Exiting program")
    GPIO.cleanup()
