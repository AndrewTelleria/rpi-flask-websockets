from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import sys
import board
import adafruit_dht
import busio
import adafruit_ccs811

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

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D27)

i2c = busio.I2C(board.SCL, board.SDA)
ccs811 = adafruit_ccs811.CCS811(i2c)

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('newdata')
def update_client_sensor_data():
    # Infinite loop to constantly update sensor data on client
    while True:
        try:
            emit('environment', {'data': 'HELLO',
                        'temperature_c': dhtDevice.temperature,
                        'temperature_f': dhtDevice.temperature * (9 / 5) + 32,
                        'humidity': dhtDevice.humidity,
                        'co2': ccs811.eco2,
                        'tvoc': ccs811.tvoc
                        })
            socketio.sleep(2)
        except:
            continue

@socketio.on('test')
def test():
    """Testing to see see if connect on the client end can run two seperate functions on connect"""
    print("While loop is initiating")
    while True:
        try:
            humidity = dhtDevice.humidity
            print("Humidity: ", humidity)
            if humidity < 80:
                print("Humidity is below 80")
                relay1.on()
                emit('power', {'message': 'Relay 1 is on'})
            elif humidity > 90:
                print("Humidity is above 90")
                relay1.off()
                emit('power', {'message': 'Relay 1 is off'})
        except:
            continue
        socketio.sleep(2)

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': message['data']})


@socketio.on('my broadcast event')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected.')

if __name__ == '__main__':
    try:
        socketio.run(app)
    except KeyboardInterrupt:
        sys.exit(0)
