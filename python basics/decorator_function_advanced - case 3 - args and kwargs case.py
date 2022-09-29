# Outer Decorator Function definition
#   As an argument function that will
#   be decorated is taken.
def before_after_decorator(function):
    # Inner Decorator Function definition (wrapper function)
    #   As an arguments may be taken the same amount of arguments as
    #   a decorated function has or special argument (*args) may
    #   be used.
    def wrapper(*args):
#   def wrapper(a, b, c): <- in a_function case it's effectively the same
        print(f"Before function")
        function(*args)
        print(f"After function")
    return wrapper

#
@before_after_decorator
def a_function(a, b, c):
#   print(f"Before function") <- effectively it works like this
    print(f"FUNCTION {a * b * c}")
#   print(f"After function)" <- effectively it works like this

a_function(2, 2, 2)