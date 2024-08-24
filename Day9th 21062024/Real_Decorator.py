#real Example
def note_time_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} executed successfully")
        return result
    return wrapper

@note_time_decorator
def log_function():
    print("Executing log_function")
log_function = note_time_decorator(log_function)
log_function()