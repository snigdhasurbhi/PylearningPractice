# DEcorators in python means essentially function that takes another function as an argument and extends its functionality
# In other words, a decorator is a function that takes another function and returns a new function that enhances the original function

# Example 1
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap
#return a function from a function

def func1():
    print("Hello")
from functools import wraps

#DEcorators return a new function with the added functionality, without modifying the original function
def decorator_function(original_function):
    def wrapper_function():
        print(f"Wrapper executed before {original_function.__name__}")
        return original_function()
    return wrapper_function