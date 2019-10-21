# def outer_func(msg):
#     def inner_func():
#         print(msg)
#     return inner_func

def decorator_func(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function')

decorated_display = decorator_func(display)
decorated_display()

# hi_func = outer_func('Hi')
# bye_func = outer_func('Bye!')
#
# hi_func() # closure
# bye_func()
