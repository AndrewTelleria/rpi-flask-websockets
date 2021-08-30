import time

class TimeError(Exception):
    """A custom exception used to report erros in use of Timer Class"""

class Timer:
    def __init__(self):
        self._start_time = None
        self._start_fans = False
        
    
    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimeError(f"Timer is running. User .stop() to stop it")
        
        self._start_time = time.perf_counter()
        print('Start time', self._start_time)
    
    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimeError(f"Timer is not running. Use .start() to start it")
        self._start_time = None
        print(f"Time stopped")

    def startFan(self):
        """Start the fans"""
        if self._start_fans is not False:
            raise TimeError(f"startFan() error")
        
        self._start_time = time.perf_counter()
        self._start_fans = True
        print('Time: {}, Start Fans: {}'.format(self._start_time, self._start_fans))
    
    def stopFan(self):
        """Stop the fans"""
        if self._start_fans is not True:
            raise TimeError(f"Timer is running. User .startFan() to start the fans")
        self.stop()
        self._start_fans = False
        print('Time: {}, Start Fans: {}'.format(self._start_time, self._start_fans))
    
    def checkElapsedTime(self):
        """Checks to see how much time has elapsed."""
        if self._start_time is None:
            raise TimeError(f"Timer is not running. Use .start() to start it")
        
        return time.perf_counter() - self._start_time