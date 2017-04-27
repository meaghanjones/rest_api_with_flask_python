#decorators are just a function that gets called before another function
#function tools library
#keep this as a template for when you need to use decorators
import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_that_runs_func

@my_decorator
def my_function():
    print("I'm the function!")

#my_function()

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func():
            print("In the decorator!")
            if number == 56:
                print("Not running the function!")
            else:
                func()
            print("After the decorator!")
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(56)
def my_function_too():
    print("Hello")

my_function_too()

#sometimes useful / ie admin pages / dont want to have duplicate code
