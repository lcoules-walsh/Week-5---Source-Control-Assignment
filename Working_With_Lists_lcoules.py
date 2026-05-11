courses = ["Introduction To Security", 
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