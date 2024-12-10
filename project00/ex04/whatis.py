import sys

def even_or_odd():
    if len(sys.argv) == 1:
        return
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    try:
    	arg = int(sys.argv[1])
    except ValueError as err:
        raise AssertionError("argument is not an integer")
    if arg == 0 or arg % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

try:
    even_or_odd()
except AssertionError as err:
    print(f"AssertionError: {err}")