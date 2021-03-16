def add (x,y):
    """Add Function"""
    return x + y
    

def subtract (x,y):
    """Subtract Fuction"""
    return x - y


def multiply (x,y):
    """multiply Fuction"""
    return x * y


def divide (x,y):
    """divide Fuction"""
    if y == 0:
        raise ValueError('can not divide zero')
    return x // y
