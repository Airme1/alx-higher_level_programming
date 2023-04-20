#!/usr/bin/python3

#Python Code to Demostrate Exception

def safe_print_division(a, b):
    try:
        result = a/b
    #If input is denominator is zero handle it with exception
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
