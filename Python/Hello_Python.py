bacon_amount = 0
print(bacon_amount)

# Ordering bacon, egg, bacon, bacon, pepperoni and bacon (4 more servings of bacon)
bacon_amount = bacon_amount + 4

if bacon_amount > 0:
    print("But I don't want ANY bacon!")

viking_song = "Bacon" * bacon_amount
print(viking_song)

print(type(bacon_amount))
print(type(20.55))

# Prints float
print(5 / 2)
print(6 / 2)

# Prints a result that is rounded down to the next integer
print(5 // 2)
print(6 // 2)

hat_height_cm = 25
my_height_cm = 190
# How am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters = ", total_height_meters, "?")

print(min(1, 2, 3))
print(max(1, 2, 3))

print(abs(32))
print(abs(-32))

print(float(10))
print(int(3.3))
print(int('101') + 1)