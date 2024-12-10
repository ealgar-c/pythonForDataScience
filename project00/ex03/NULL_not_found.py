import math

def NULL_not_found(object: any) -> int:
    nnull = True if object else False
    if type(object).__name__ == "float" and math.isnan(object):
        print(f"Cheese : {object} {type(object)}")
        return 0
    if nnull:
        print("Type not found")
        return 1
    if type(object).__name__ == "NoneType":
        print(f"Nothing : {object} {type(object)}")
    elif type(object).__name__ == "int":
        print(f"Zero : {object} {type(object)}")
    elif type(object).__name__ == "str":
        print(f"Empty : {object} {type(object)}")
    elif type(object).__name__ == "float":
        print(f"Cheese : {object} {type(object)}")
    elif type(object).__name__ == "bool":
        print(f"Fake : {object} {type(object)}")
    return 0