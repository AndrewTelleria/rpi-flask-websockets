import gpiozero
import time

RELAY_1 = 14
RELAY_2 = 15
RELAY_3 = 18
RELAY_4 = 23
RELAY_5 = 17
RELAY_6 = 27
RELAY_7 = 22
RELAY_8 = 24

relay1 = gpiozero.OutputDevice(RELAY_1, active_high=False, initial_value=False)
relay2 = gpiozero.OutputDevice(RELAY_2, active_high=False, initial_value=False)
relay3 = gpiozero.OutputDevice(RELAY_3, active_high=False, initial_value=False)
relay4 = gpiozero.OutputDevice(RELAY_4, active_high=False, initial_value=False)
relay5 = gpiozero.OutputDevice(RELAY_5, active_high=False, initial_value=False)
relay6 = gpiozero.OutputDevice(RELAY_6, active_high=False, initial_value=False)
relay7 = gpiozero.OutputDevice(RELAY_7, active_high=False, initial_value=False)
relay8 = gpiozero.OutputDevice(RELAY_8, active_high=False, initial_value=False)

print('Starting relay test')

relay1.on()
time.sleep(5)
relay1.off()
time.sleep(5)

relay2.on()
time.sleep(5)
relay2.off()
time.sleep(5)

relay3.on()
time.sleep(5)
relay3.off()
time.sleep(5)

relay4.on()
time.sleep(5)
relay4.off()
time.sleep(5)

relay5.on()
time.sleep(5)
relay5.off()
time.sleep(5)

relay6.on()
time.sleep(5)
relay6.off()
time.sleep(5)

relay7.on()
time.sleep(5)
relay7.off()
time.sleep(5)

relay8.on()
time.sleep(5)
relay8.off()
time.sleep(5)

print('Finished test')
