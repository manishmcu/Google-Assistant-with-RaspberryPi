import random
import sys
import time
from Adafruit_IO import MQTTClient

import requests

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
    
def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, status):
    print('Feed {0} received new value: {1}'.format(feed_id, status))
    
    if feed_id == 'Relay 1':
        if status == "1":
            print("Bed light ON")
        else:
            print("Bed light OFF")
    if feed_id == 'Relay 2':
        if status == "1":
            print("Light ON")
        else:
            print("Light OFF")
        
       # requests.post('{0}/widgets/slider'.format(DASHBOARD_URL), data={'value': payload})
    #elif feed_id == 'pi-dashboard-humidity':
        #requests.post('{0}/widgets/humidity'.format(DASHBOARD_URL), data={'value': payload})
   # elif feed_id == 'pi-dashboard-temp':
       # requests.post('{0}/widgets/temp'.format(DASHBOARD_URL), data={'value': payload})


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

client.connect()

client.loop_blocking()
