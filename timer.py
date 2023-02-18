import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None
        self._total_time = 0

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is already running")
        self._start_time = time.time()

    def stop(self):
        """Stop the timer, and add the elapsed time to the total time"""
        if self._start_time is None:
            raise TimerError("Timer is not running")
        elapsed_time = time.time() - self._start_time
        self._total_time += elapsed_time
        self._start_time = None

    def reset(self):
        """Reset the timer"""
        self._start_time = None
        self._total_time = 0

    def total(self):
        """Return the total elapsed time"""
        return self._total_time
