def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    # return inner_func()
    # the above line returns the function and executes the function
    # the line below just returns the function
    return inner_func

# outer_func()
# my_func = outer_func()
# print(my_func.__name__) # inner_func
# my_func is equal to the inner func
# my_func() # Hi

# A closure is an inner function that remembers and has access to variables
# in the local scope in which it was created even after the outer function has
# finished executing.

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func() # Hi
hello_func() # Hello

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(f"Running \"{func.__name__}\" with arguments {args}")
        #logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)
