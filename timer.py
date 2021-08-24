import time

class TimeError(Exception):
    """A custom exception used to report erros in use of Timer Class"""

class Timer:
    def __init__(self):
        self._start_time = None
        self._start_fans = None
        
    
    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimeError(f"Timer is running. User .stop() to stop it")
        
        self._start_time = time.perf_counter()
        print(self._start_time)
    
    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimeError(f"Timer is not running. Use .start() to start it")
        
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")

    def startFan(self):
        """Start the fans"""
        if self._start_fans is not None:
            raise TimeError(f"Timer is running. User .stopFan() to stop the fans")
        
        self._start_time = time.perf_counter()
        self._start_fans = True
        print(self._start_time)
    
    def stopFan(self):
        """Stop the fans"""
        if self._start_fans is not None:
            raise TimeError(f"Timer is running. User .stopFan() to stop the fans")
        
        self._start_time = None
        self._start_fans = False
    
    def checkElapsedTime(self):
        """Checks to see how much time has elapsed."""
        if self._start_time is None:
            raise TimeError(f"Timer is not running. Use .start() to start it")
        
        return time.perf_counter() - self._start_time