import datetime

from pyutils.misc.timer import Timer


def test_time():
    with Timer() as timer:
        pass

    assert isinstance(timer.start_time, (datetime.datetime,))
    assert isinstance(timer.end_time, (datetime.datetime,))
    assert isinstance(timer.duration, (datetime.timedelta,))
