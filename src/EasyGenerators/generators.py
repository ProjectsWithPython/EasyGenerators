def odd_generator(min: int, max: int):
    """Generator for odd number"""
    try:
        for number in range(min, max):
            if number % 2 != 0:
                yield number
    except:
        return "Error, please check your args"

def even_generator(min: int, max: int):
    """Generator for even numbers"""
    try:
        for i in range(min, max):
            if i % 2 == 0:
                yield i
    except:
        return "Error, please check your args"


def add_five_generator(min, max):
    """Adds five to every number"""
    try:
        for i in range(min, max):
            i += 5
            yield i
    except:
        return "Error, please check your args"


def custom_generator(min : int, max :int, divisable_by : int):
    """Make your own generator"""
    try:
        for i in range(min, max):
            if i % divisable_by == 0:
                yield i
    except ZeroDivisionError:
        return "divisable_by cannot be 0"
    except:
        return "Error, please check your args"