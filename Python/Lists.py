primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# List of lists
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K']
]

my_faourites = [32, 'books', help]

# Indexing
print(planets[0])
print("What is the next closest planet?", planets[1])
print("Which planet is the furthest form the sun?", planets[-1])

# Slicing
print("What are the first three planets?", planets[0:3])
# or can be printed as
print("What are the first three planets?", planets[:3])
""" If I leave out the end index, it's assumed to be the length of the list, i.e. the expression above means "give me all the planets from index 3 onward".
"""
print(planets[3:])
# Negative indices when slicing
# All the planets except the first and last
print(planets[1:-1])
# The last 3 planets
print(planets[-3:])

# Changing lists
planets[3] = "Malacandra"
print(planets)

# List functions
print("Number of planets = ", len(planets))
print("Sorted planets: ", sorted(planets))

primes = [2, 3, 5, 7]
print(sum(primes))
print(max(primes))

# Objects
x = 12
# x is a real number, so its imaginary part is 0
print(x.imag)
# Making a complex number
c = 12 + 3j
print(c.imag)

# List methods
planets.append('Pluto')
help(planets.append)
print("New list of planets: ", planets)
planets.pop()
print("Popped list of planets: ", planets)

# Searching lists
print(planets.index('Earth'))
# Is Earth a planet?
print("Earth" in planets)
# Is Calbefraques a planet?
print("Calbefraques" in planets)

# Tuples
t = (1, 2, 3)
t = 1, 2, 3
print(t)

x = 0.125
print(x.as_integer_ratio())

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

a = 1
b = 0
a, b = b, a
print(a, b)