from custom_errors import CustomZeroDivision
def divide(a,b):
    try:
        c = a/b
    except ZeroDivisionError as e:
        raise CustomZeroDivision('this is my custom zero division error')
    return c