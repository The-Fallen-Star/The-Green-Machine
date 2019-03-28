import RPi.GPIO as GPIO
import time
#setup stuff
PIN_TRIGGER = 17 #trigger pin for ultrasonic sensor
PIN_ECHO = 27 #echo pin for ultrasonic sensor
GPIO.setmode(GPIO.BCM) #chooses how pins are assigned/ declared
GPIO.setup(PIN_TRIGGER, GPIO.OUT) #triggar pin declared as output
GPIO.setup(PIN_ECHO, GPIO.IN) #echo pin declared as input

GPIO.setup(26, GPIO.OUT) #declares 26,19,13 as output, for servo motors
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)


#distance method, returns distance in cm, requires about .5 seconds to run
def getDistance():
    try:
          GPIO.output(PIN_TRIGGER, GPIO.LOW)
          time.sleep(.4)
          GPIO.output(PIN_TRIGGER, GPIO.HIGH)
          time.sleep(0.00001)
          GPIO.output(PIN_TRIGGER, GPIO.LOW)
          while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
          while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()
          pulse_duration = pulse_end_time - pulse_start_time
          distance = round(pulse_duration * 17150, 2)
    finally:     
        return distance;
    
#invoke trash method to open trash bin, open for 3 seconds, closed for 3 seconds
def trash():
    tras = GPIO.PWM(26, 50)
    tras.start(5.2)
    tras.ChangeDutyCycle(5.2)
    time.sleep(3)
    tras.ChangeDutyCycle(10.2)
    time.sleep(3)
    tras.stop()
    time.sleep(1)
    return;

#invoke Compost method to open compost bin, open for 3 seconds, closed for 3 seconds
def compost():
    comp = GPIO.PWM(19, 50)
    comp.start(5.1)
    comp.ChangeDutyCycle(5.1)
    time.sleep(3)
    comp.ChangeDutyCycle(10)
    time.sleep(3)
    comp.stop()
    time.sleep(1)
    return;

#invoke recycle method to open recycle bin, open for 3 seconds, closed for 3 seconds
def recycle():
    recy = GPIO.PWM(13, 50)
    recy.start(5.3)
    recy.ChangeDutyCycle(5.3)
    time.sleep(3)
    recy.ChangeDutyCycle(10.25)
    time.sleep(3)
    recy.stop()
    time.sleep(1)
    return;


#testing below and where our actual code will be
while True: #just an infinite loop
    distance=getDistance() #assigns 'distance' with ultrasonic reading 
    print(distance) #prints distance
    if distance<12: #if discance is <12cm, defaults to opening trash bin
        trash()


#required at end
GPIO.cleanup()
