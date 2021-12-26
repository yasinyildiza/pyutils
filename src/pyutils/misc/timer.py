import datetime


class Timer:
    """
    Context manager to measure the amount of time
    for the execution in the scope

    Usage:

    with Timer() as timer:
        # do your magic within the scope of the context manager
        my_function()

    # `timer.duration` will return a `datetime.timedelta` object
    # that holds the duration of the execution
    print(f'my_function() took f{timer.duration.total_seconds()} seconds')
    """

    def now(self) -> datetime.datetime:
        return datetime.datetime.now()

    def __enter__(self) -> "Timer":
        self._start_time = self.now()
        self._end_time = None

        return self

    def __exit__(self, type, value, traceback):
        self._end_time = self.now()

    @property
    def start_time(self) -> datetime.datetime:
        return self._start_time

    @property
    def end_time(self) -> datetime.datetime:
        return self._end_time

    @property
    def duration(self) -> datetime.timedelta:
        return self.end_time - self.start_time
