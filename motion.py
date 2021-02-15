import RPi.GPIO as GPIO
import time
 
SENSOR_PIN = 12
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR_PIN, GPIO.IN)
 
def my_callback(channel):
    # Here, alternatively, an application / command etc. can be started.
    print('There was a movement rising!')

def my_callback2(channel):
    # Here, alternatively, an application / command etc. can be started.
    print('There was a movement falling!')

try:
    #GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=my_callback)
    #GPIO.add_event_detect(SENSOR_PIN , GPIO.FALLING, callback=my_callback2)
    while True:
        value = GPIO.input(SENSOR_PIN)
        print ('value ' + str(value))
        time.sleep(10) #sensor has a 5-6 seconds reset after each read. Also 30-60 seconds before sensor works properly after first powered up
except KeyboardInterrupt:
    print ('Finish...')
    GPIO.cleanup()
GPIO.cleanup()