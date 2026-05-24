import math
import numpy

print("It's math! It has type {}".format(type(math)))
print(dir(math))

print("pi to 4 significant digits = {:.4}".format(math.pi))

print(math.log(32, 2))
print(math.pi)

print("numpy.random is a ", type(numpy.random))
print("it contains names such as...", dir(numpy.random)[-15:])

rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

# type()
print(type(rolls))

# dir()
print(dir(rolls))
print(rolls.mean())
print(rolls.tolist())

# Operator overloading
print(rolls + 10)
print(rolls <= 3)

xlist = [[1,2,3],[2,4,6]]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx = \n{}".format(xlist, x))
print(x[1,-1])

# Tensorflow
import tensorflow as tf
# Create two constants, each with value 1
a = tf.constant(1)
b = tf.constant(1)
print(a+b)

# Get the rows with population over 1m in South America
df[(df['population'] > 10**6) & (df['continent'] == 'South America')]
print(dir(list))