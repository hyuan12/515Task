import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None
        self._elapsed_time = 0

    def start(self):
        if self._start_time is not None:
            raise TimerError("timer is already running")
        self._start_time = time.monotonic()

    def stop(self):
        if self._start_time is None:
            raise TimerError("timer is not running")
        elapsed_time = time.monotonic() - self._start_time
        self._elapsed_time += elapsed_time
        self._start_time = None

    def reset(self):
        # self._start_time = None
        # self._elapsed_time = 0
        self._elapsed_time = 0

    def total(self):
        if self._start_time is not None:
            current_elapsed_time = time.monotonic() - self._start_time
            return self._elapsed_time + current_elapsed_time
        else:
            return self._elapsed_time
