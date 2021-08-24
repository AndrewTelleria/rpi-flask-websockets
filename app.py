from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import sys
import board
import busio
import adafruit_scd30
import math

import gpiozero

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

RELAY_1 = 5
RELAY_2 = 6
RELAY_3 = 13
RELAY_4 = 16
RELAY_5 = 19
RELAY_6 = 20
RELAY_7 = 21
RELAY_8 = 26

relay1 = gpiozero.OutputDevice(RELAY_1, initial_value=False)
relay2 = gpiozero.OutputDevice(RELAY_2, initial_value=False)
relay3 = gpiozero.OutputDevice(RELAY_3, initial_value=False)
relay4 = gpiozero.OutputDevice(RELAY_4, initial_value=False)
relay5 = gpiozero.OutputDevice(RELAY_5, initial_value=False)
relay6 = gpiozero.OutputDevice(RELAY_6, initial_value=False)
relay7 = gpiozero.OutputDevice(RELAY_7, initial_value=False)
relay8 = gpiozero.OutputDevice(RELAY_8, initial_value=False)

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
scd = adafruit_scd30.SCD30(i2c)

"""dictionary for the relays that have the first value for power 
and the second value is if the power is overrided by the user
default is False"""
relays = {
    'relay1': [False, relay1, 'automate'],
    'relay2': [False, relay2, 'automate'],
    'relay3': [False, relay3, 'automate'],
    'relay4': [False, relay4, 'automate'],
    'relay5': [False, relay5, 'automate'],
    'relay6': [False, relay6, 'automate'],
    'relay7': [False, relay7, 'automate'],
    'relay8': [False, relay8, 'automate']
}

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('newdata')
def update_client_sensor_data():
    # Infinite loop to constantly update sensor data on client
    while True:
        data = scd.data_available
        if data:
            humidity = scd.relative_humidity
            temp = scd.temperature
            co2 = scd.CO2
            try:
                emit('environment', {'data': 'HELLO',
                            'temperature_c': temp,
                            'temperature_f': temp * (9 / 5) + 32,
                            'humidity': humidity,
                            'co2': co2,
                            })
                socketio.sleep(2)
            except:
                continue

@socketio.on('test')
def relay_board_init():
    """Testing to see see if connect on the client end can run two seperate functions on connect"""
    print("While loop is initiating")
    while True:
        try:
            data = scd.data_available
            if data:
                humidity = scd.relative_humidity
                temp_c = scd.temperature
                co2 = scd.CO2
                print("Humidity: ", humidity)
                
                if humidity < 95 and relays['relay3'][2] != 'override':
                    """Turn on the humidifier: two ultrasonic mist makers, one computer fan"""
                    print("Humidity is below 80")
                    relay3.on()
                    relays['relay3'][0] = True
                elif humidity > 99 and relays['relay3'][2] != 'override':
                    """Turn off the humidifier"""
                    print("Humidity is above 90")
                    relay3.off()
                    relays['relay3'][0] = False
                if temp_c < 24 and relays['relay5'][2] != 'override':
                    """Turn on the space heater to keep temperature around 24 to 27 celsius"""
                    print("Temperature >>> ", temp_c)
                    relay5.on()
                    relays['relay5'][0] = True
                elif temp_c > 27 and relays['relay5'][2] != 'override':
                    relay5.off()
                    relays['relay5'][0] = False
                if co2 > 5000 and relays['relay4'][2] != 'override':
                    """Turn on air exchange system: two duct fans, one clip fan"""
                    print("co2 is more than 5000")
                    relay4.on()
                    relays['relay4'][0] = True
                elif co2 < 5000 and relays['relay4'][2] != 'override':
                    relay4.off()
                    relays['relay4'][0] = False
                """Give a serializeable JSON object to pass to the client.
                Since there is a function referenced in the relay dict
                it cannot be serialized"""
                data = {}
                for item in relays.items():
                    data[item[0]] = [item[1][0], item[1][2]]
                emit('power', {'relays': data})

        except Exception as e:
            print(e)
            continue
        socketio.sleep(2)


@socketio.on('power override')
def override_on_off(relay):
    """Override function is called when the user presses the on/off button on the client
    next(iter(relay)) is a function to retrieve the first item of the dictionary
    and there is one item received from client."""
    print('Data received: ', next(iter(relay)))
    data = next(iter(relay))
    value = relay[data]
    if value == True:
        relays[data][0] = True
        relays[data][1].on()
    else:
        relays[data][0] = False
        relays[data][1].off()
    relays[data][2] = 'override'

@socketio.on('power automate')
def override_on_off(relay):
    """Set the system back to automated"""
    print('Data received: ', next(iter(relay)))
    data = next(iter(relay))
    value = relay[data]
    relays[data][2] = value
        

if __name__ == '__main__':
    try:
        socketio.run(app)
    except KeyboardInterrupt:
        sys.exit(0)
