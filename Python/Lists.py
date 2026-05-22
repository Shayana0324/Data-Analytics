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
print("What are the first three planets?", planets[0:3])
# or can be printed as
print("What are the first three planets?", planets[:3])
# If I leave out the end index, it's assumed to be the length of the list, i.e. the expression above means "give me all the planets from index 3 onward".
print(planets[3:])
# Negative indices when slicing
# All the planets except the first and last
print(planets[1:-1])
# The last 3 planets
print(planets[-3:])

# Changing lists