from time import sleep
import RPi.GPIO as GPIO

DIR = 20  # Direction GPIO Pin
STEP = 21 # Step GPIO Pin
CW = 1    # Clockwise Rotation
CCW = 0   # Counterclockwise Rotation
SPR = 200  # Steps per Revolution 360/1.8 = 200

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
delay = 0.005

def rotate(step_list):
    for steps in step_list:
        if steps > 0:
            GPIO.output(DIR, CCW)
            for x in range(steps):
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)
                
        if steps < 0:
            GPIO.output(DIR, CW)
            for x in range(-steps):
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)

        sleep(0.5)

step_list = [200, -200, 120, 15, -60, 500, -30]

rotate(step_list)
        
GPIO.cleanup()
