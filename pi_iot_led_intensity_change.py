import random
import sys
import time
from Adafruit_IO import MQTTClient

import requests
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

my_pwm_5=GPIO.PWM(5,100)
my_pwm_5.start(100)

my_pwm_7=GPIO.PWM(7,100)
my_pwm_7.start(100)

ADAFRUIT_IO_KEY      = 'aio_cEQk60uNwKank8nAXtPXP1Ps5LJ0'       # Set to your Adafruit IO key.
ADAFRUIT_IO_USERNAME = 'Debanik2000'  # See https://accounts.adafruit.com
                                                    # to find your username.
# Set the URL of the physical dashboard to use.  If running on the same Pi as
# the dashboard server then keep this the default localhost:5000 value.  If
# modified make sure not to end in a slash!
#DASHBOARD_URL = 'http://localhost:5000'  # URL of the physical dashboard.
                                         # Don't end with a slash!


# Define callback functions which will be called when certain events happen.
def connected(client):
    print('Connected to Adafruit IO!  Listening for feed')
    client.subscribe('Relay 1')
    client.subscribe('Relay 2')
    client.subscribe('Relay 3')
    client.subscribe('Relay 4')
    client.subscribe('Relay 5')
    
def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, status):
    print('Feed {0} received new value: {1}'.format(feed_id, status))
    
    if feed_id == 'Relay 1':
        if status == "1":
            print("Bed light ON by google")
            my_pwm_7.ChangeDutyCycle(100)
        else:
            print("Bed light OFF by goole")
            my_pwm_7.ChangeDutyCycle(0)
            
    if feed_id == 'Relay 2':
        if status == "1":
            print("Light ON by alexa")
            my_pwm_5.ChangeDutyCycle(100)
        else:
            print("Light OFF by alexa")
            my_pwm_5.ChangeDutyCycle(0)
    if feed_id == 'Relay 3':
        if status == "1":
            print("High light intensity by goole")
            my_pwm_7.ChangeDutyCycle(100)
        else:
            print("Low light intensity by google")
            my_pwm_7.ChangeDutyCycle(5)
    if feed_id == 'Relay 5':
        if status == "1":
            print("High light intensity by alexa")
            my_pwm_5.ChangeDutyCycle(100)
        else:
            print("Low light intensity by alexa")
            my_pwm_5.ChangeDutyCycle(5)
    if feed_id == 'Relay 4':
        if status == "1":
            print("medium intensity by goole")
            my_pwm_7.ChangeDutyCycle(45)
        else:
            print("medium intensity by alexa")
            my_pwm_5.ChangeDutyCycle(45)
        
        
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

client.connect()

client.loop_blocking()
GPIO.cleanup()