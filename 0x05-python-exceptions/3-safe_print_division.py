#!/usr/bin/python3

# Python Code to Demostrate Exception

def safe_print_division(a, b):
    try:
        result = a / b
    # If denominator is zero or not integer handle it with exception
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
