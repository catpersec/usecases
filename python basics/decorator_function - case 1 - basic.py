import time


# 1. Defining Decorator Function
#   a) Defining wrap function that takes function
#      that is to be decorated and gives it additional
#      functionality
# 2. Defining Function with @decorator function above
#   a) Interesting thing is that there is no straight
#      reference like delay_function(say_hello)
# 3. Call function that is decorated


# 1
def delay_function(function):
    # a
    def wrapper_function():
        time.sleep(2)
        function()
        print("i'm wrap :s")

    return wrapper_function


# 2 and #a
@delay_function
def say_hello():
    print("Hello world!")


# 3
say_hello()
