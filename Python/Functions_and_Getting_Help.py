"""
help() displays two things:

the header of that function round(number, ndigits=None). In this case, this tells us that round() takes an argument we can describe as number. Additionally, we can optionally give a separate argument which could be described as ndigits.
A brief English description of what the function does.
"""
# help(round(-2.01))
# help(print)

# Defining functions
def least_diff(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(
    least_diff(1, 10, 100),
    print(1, 10, 10),
    least_diff(5, 6, 7)
)

# help(least_diff)

# Functions applied to functions
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n'
)

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is the biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n'
)