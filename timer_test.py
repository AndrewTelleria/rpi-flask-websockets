import time
from timer import Timer

timer = Timer()
timer.start()


while True:
    print(timer.checkElapsedTime())
    # Check to see if the time has elapsed 5 minutes
    if timer.checkElapsedTime() >= 10 and timer._start_fans == False:
        timer.startFan()
        # Check to see if the fans are on and have been running for a minute a more
    elif timer.checkElapsedTime() >= 5 and timer._start_fans == True:
        timer.stopFan()
        timer.start()
    time.sleep(1)