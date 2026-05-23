x = 'Pluto is a planet'
y = 'Pluto is a planet'
print(x == y)

print("Pluto's a planet!")
print('My dog is named "Pluto"')

print('Pluto\'s a planet!')

hello = "hello\nworld"
print(hello)

triplequoted_hello = """hello
world"""
print(triplequoted_hello)
print(triplequoted_hello == hello)

print("hello")
print("world")
print("hello", end='')
print("pluto", end='')
print("\n")

planet = 'Pluto'
print(planet[0])
print(planet[-3:])
print(len(planet))

print([char+'!' for char in planet])

# Cannot modify strings like we modify lists - they are immutable

claim = "Pluto is a planet!"
print(claim.upper())
print(claim.lower())

# Searching for the first index of a substring
print(claim.index('plan'))
print(claim.startswith(planet))
print(claim.endswith('planet'))

# String split and join
words = claim.split()
print(words)

datestr = '1999-03-24'
year, month, day = datestr.split('-')
print(year, month, day)

print('/'.join([month, day, year]))

# Unicode characters in string literals
print(' 👏 '.join([word.upper() for word in words]))

# Building strings with .format()
print(planet + ', you are missed.')

# Calling non-string objects with a string
position = 9
print(planet + ", you'll awalys be the " + str(position) + "th planet.")
# str.format() for easier typing
print("{}, you'll always be the {}th planet.".format(planet, position))

pluto_mass = 1.303 * 10 **22
earth_mass = 5.9722 * 10**24
population = 52910390
# 2 decimal points, 3 decimal points, format as percent   separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonian.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population
))
# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

# Dictionaries
numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])
numbers['eleven'] = 11
print(numbers)
numbers['one'] = 'Pluto'
print(numbers)
# Python has dictionary comprehensions with a syntax similar to the list comprehensions
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)
# The in operator tells us whether something is a key in the dictionary
print('Saturn' in planet_to_initial)
print('Betelguese' in planet_to_initial)
# A for loop over a dictionary will loop over its keys
for k in numbers:
    print("{} = {}".format(k, numbers[k]))
# We can access a collection of all the keys or all the values with dict.keys() and dict.values(), respectively.
# Get all the initials, sort them alphabetically, and put them in a space-separated string.
print(' '.join(sorted(planet_to_initial.values())))
'''The very useful dict.items() method lets us iterate over the keys and values of a dictionary simultaneously. (In Python jargon, an item refers to a key, value pair)'''
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
    
