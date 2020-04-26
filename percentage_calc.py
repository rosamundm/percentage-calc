# float (decimal percentage) of x = y
def percent_of_is(float, x):
    y = float * x
    return y

print(percent_of_is(0.25, 30))



# x is percentage% of y
def is_percent_of(x, y):
    percentage = x * 100 / y
    return percentage

print(is_percent_of(1, 4))
