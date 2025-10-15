from functools import wraps
import time

def timestamp(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(time.ctime())
        return func(*args, **kwargs)
    return wrapper
