# Problem 4-1 lcoules

places = [
    "Tokyo",
    "New York",
    "Georgia",
    "France"
]

for place in places:
    print(place + " is a nice place to visit")

# Problem 4-2

for number in range(90, 101):
    print(number)

# Problem 4-3

large_numbers = list(range(100000, 1000001))

print("Sum of numbers:", sum(large_numbers))

# Problem 4-4

random_numbers = [
    54, 17, 87, 33, 91,
    4, 59, 61, 100, 32,
    12, 76, 16, 8, 2,
    97, 94, 46, 39, 21
]

print("Largest number:", max(random_numbers))
print("Smallest number:", min(random_numbers))

# Problem 4-5

multiples_of_five = list(range(5, 101, 5))

print(multiples_of_five)

# Problem 4-6

values = list(range(20, 31))

print(values)

doubled_values = [value * 2 for value in values]

print(doubled_values)

# Problem 4-7

print("First 2 values:")
print(random_numbers[:2])

print("Items 5-10:")
print(random_numbers[4:10])

print("Last 4 items:")
print(random_numbers[-4:])

# Problem 4-8

bands = ["Linkin Park", "Metallica", "Imagine Dragons"]

copied_bands = bands[:]

bands.append("Five Finger Death Punch")

print("Original list:")
print(bands)

print("Copied list:")
print(copied_bands)

# Problem 4-9

grades = ("1st", "2nd", "3rd", "4th", "5th")

# Tuples cannot be modified, therfore causing an error
#grades[0] = "6th"

print(grades)