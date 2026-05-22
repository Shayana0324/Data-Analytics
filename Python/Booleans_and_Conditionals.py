x = True
print(x)
print(type(x))

def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says one must be at least 35 years old
    return is_natural_born_citizen and (age >= 35)

print("Can a 19-year old run for president?", can_run_for_president(19, True))
print("Can a 45-year old run for president?", can_run_for_president(45, False)) 
print("Can a 45-year old run for president?", can_run_for_president(45, True)) 

def is_odd(n):
    return (n % 2) == 1

print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))

def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else: 
        print(x, "is unlike anything I have ever seen....")

inspect(0)
inspect(15)


# Boolean conversion
print(bool(1))          # All numbers are treated as true, except 0
print(bool(0))
print(bool("the"))      # All strings are treated as true, except the empty string ""
print(bool(""))

if 0:
    print(0)
elif "spam":
    print("spam")