import time


def start_timer():

    return time.time()


def end_timer(start_time):

    return round(
        time.time() - start_time,
        2
    )