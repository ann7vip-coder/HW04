from functools import wraps

def allcaps(func):
    @wraps(func)
    def wrapper():
        result = func()  # function has no arguments per spec
        return result.upper() if isinstance(result, str) else result
    return wrapper
