# -------------------------------------------------
# Requirement #1
# Create a list of completed Walsh College courses
# -------------------------------------------------

courses = [
    "introduction to security",
    "networks & operating systems",
    "bus communication strategies",
    "fund of cyber security",
    "server virt & perf engine",
    "ethical hacking strat & tools"
]

# -------------------------------------------------
# Requirement #2
# Sort the list and print each course in uppercase
# -------------------------------------------------

courses.sort()

for course in courses:
    print(f"I have taken {course.upper()} at Walsh College.")

# -------------------------------------------------
# Requirement #3
# Add upcoming courses, re-sort, and print list
# -------------------------------------------------

courses.append("db design & development")
courses.append("advanced programming")
courses.append("digital and network forensics")

courses.sort()

print("\nThis is my course of study with upcoming courses added:")

for course in courses:
    print(course)

# -------------------------------------------------
# Requirement #4
# Remove completed courses and print removed courses
# -------------------------------------------------

taken_courses = [
    "introduction to security",
    "networks & operating systems",
    "bus communication strategies",
    "fund of cyber security",
    "server virt & perf engine",
    "ethical hacking strat & tools"
]

print("\nI do not have to take these courses:")

for course in taken_courses:
    print(course)
    courses.remove(course)

# -------------------------------------------------
# Requirement #5
# Print remaining upcoming courses
# -------------------------------------------------

print("\nI plan to take the following courses next term")

for course in courses:
    print(course)

# -------------------------------------------------
# Requirement #6
# Create a list of numbers divisible by 6
# -------------------------------------------------

numbers = [num for num in range(1, 1001) if num % 6 == 0]

# -------------------------------------------------
# Requirement #7
# Print first 20 numbers divisible by 6
# -------------------------------------------------

print("\nHere are twenty numbers divisible by 6.")

for number in numbers[:20]:
    print(number)

# -------------------------------------------------
# Requirement #8
# Find and store maximum number
# -------------------------------------------------

max_number = max(numbers)

print(f"\nThe maximum value in the list is: {max_number}")

# -------------------------------------------------
# Requirement #9
# Sum values between the 10th and 50th values
# -------------------------------------------------

sum_values = sum(numbers[9:50])

print(f"Here is the sum of several values in the list: {sum_values}")

# -------------------------------------------------
# Requirement #10
# Overwrite courses variable with numbers list
# -------------------------------------------------

courses = numbers