def logging_decorator(fn):
    function_name = fn.__name__
    def wrapper(*args, **kwargs):
        function_args = args
        print(f"You called {function_name}{function_args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper

#
@logging_decorator
def a_function(a, b, c):
    print(a*b*c)
    return a * b * c


a_function(1, 2, 3)
