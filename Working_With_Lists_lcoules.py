
#1 Creates a list of courses taken at Walsh College
courses = [
       "introduction to security", 
       "networks & operating Systems", 
       "bus communication strategies", 
       "fund of cyber security", 
       "server virt & perf engine", 
       "ethical hacking strat & tools"
    ]

#2 Sorts the list and prints each couse in uppercase
courses.sort()

for course in courses:
    print(f"I have taken {course.upper()} at Walsh College.")


#3 Adds upcoming courses, re-sorts, and prints the list
courses.append("advanced programming")
courses.append("db design & development")
courses.append("digital & network forensics")

print("This is my course of with upcoming courses added:")

courses.sort()

print("\nThis is my course of study with upcoming courses added:")

for course in courses:
    print(course)

#4 Removes courses already taken and print removed courses
taken_courses = [
       "introduction to security", 
       "networks & operating systems", 
       "bus communication strategies", 
       "fund of cyber security", 
       "server virt & perf wngine", 
       "ethical hacking strat & tools"
    ]

print("\nI do not have to take these courses:")

for course in taken_courses:
    print(course)
    courses.remove(course)

#5 Prints remaining courses planned for next semester
print("\nI plan to take the following courses next term:")

for course in courses:
    print(course)

#6 Creates a list of numbers from 1 to 1000 divisible by 6
numbers = []
for num in range(1, 1001):
    if num % 6 == 0:
        numbers.append(num)

#7 Prints first 20 numbers divisible by 6
print("\nHere are twenty numbers divisible by 6.")

for num in numbers[:20]:
    print(num)

#8 Prints max number in the list
max_number = max(numbers)

print(f"\nThe maximum value  in this list is: {max_number}")

#9 Calculates the sum between the 10th andd 50th values
sum_values = sum(numbers[9:50])

print(f"\nHere is the sum of several values in the list: {sum_values}")

#10 Overwrites courses variable with numbers list
courses = numbers