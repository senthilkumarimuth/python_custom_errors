from custom_errors import RateLimitHere
def divide(a,b):
    try:
        c = a/b
    except ZeroDivisionError as e:
        raise RateLimitHere('RATE EXCEEDED')
    return c