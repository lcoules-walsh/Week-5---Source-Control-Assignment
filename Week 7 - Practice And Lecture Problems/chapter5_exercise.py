# Logan Coules

# 5-1

# I predict the expression below will evaluate to True
color = "blue"
print(color == "blue")

# I predict the expression below will evaluate to False
number = 10
print(number < 5)

# I predict the expression below will evaluate to True
name = "Logan"
print(name != "LeBron")

# I predict the expression below will evaluate to False
temperature = 75
print(temperature == 100)

# I predict the expression below will evaluate to True
is_student = True
print(is_student == True)

# I predict the expression below will evaluate to False
fruit = "apple"
print(fruit == "banana")

# 5-2

# This evaluates to True
number1 = 7

if number1 % 2 == 1:
    print(str(number1) + " is odd")

# This evaluates to False
number2 = 8

if number2 % 2 == 1:
    print(str(number2) + " is odd")

# 5-3

# Odd number example
number3 = 15

if number3 % 2 == 1:
    print(str(number3) + " is odd")
else:
    number3 += 1
    print(number3)

# Even number example

number4 = 20
if number4 % 2 == 1:
    print(str(number4) + " is odd")
else:
    number4 += 1
    print(number4)

# 5-4

favorite_fruit = ["apple", "banana", "orange", "grape"]

if len(favorite_fruit) == 2:
    print("You like two fruits")

elif len(favorite_fruit) == 3:
    print("You like three fruits")

elif len(favorite_fruit) == 4:
    print("You like four fruits")

else:
    print("You like several fruits")

# 5-5

numbers = list(range(1, 56))

number_a = 25
number_b = 70

if number_a in numbers:
    print(str(number_a) + " is in the list of numbers")
else:
    print(str(number_a) + " is not in the list of numbers")

if number_b in numbers:
    print(str(number_b) + " is in the list of numbers")
else:
    print(str(number_b) + " is not in the list of numbers")

