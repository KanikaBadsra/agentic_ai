import time

from app.observability.logger import logger


def track_time(node_name):

    def decorator(func):

        def wrapper(*args, **kwargs):

            start_time = time.time()

            result = func(*args, **kwargs)

            end_time = time.time()

            execution_time = round(
                end_time - start_time,
                2
            )

            logger.info(
                f"{node_name} execution time: "
                f"{execution_time} sec"
            )

            return result

        return wrapper

    return decorator