courses = [
       "Introduction To Security", 
       "Networks & Operating Systems", 
       "Bus Communication Strategies", 
       "Fund Of Cyber Security", 
       "Server Virt & Perf Engine", 
       "Ethical Hacking Strat & Tools"
    ]

courses.sort()

for course in courses:
    print(f"I have taken {course.upper()} at Walsh College.")

courses.append("Advanced Programming")
courses.append("DB Design & Development")
courses.append("Digital & Network Forensics")

print("This is my course of with upcoming courses added:")

courses.sort()

print("\nThis is my course of study with upcoming courses added:")

for course in courses:
    print(course)

taken_courses = [
       "Introduction To Security", 
       "Networks & Operating Systems", 
       "Bus Communication Strategies", 
       "Fund Of Cyber Security", 
       "Server Virt & Perf Engine", 
       "Ethical Hacking Strat & Tools"
    ]

print("\nI do not have to take these courses:")

for course in taken_courses:
    print(course)
    courses.remove(course)

print("\nI plan to take the following courses next term:")

for course in courses:
    print(course)

numbers = []
for num in range(1, 1001):
    if num % 6 == 0:
        numbers.append(num)

print("\nHere are twenty numbers divisible by 6.")

for num in numbers[:20]:
    print(num)