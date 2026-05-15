#1 List with mixed data - lcoules

employee_data = [
    1121, "Jackie Grainger", 22.25,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.75, 1152, "David Toma"
]

#2 Sort data into separate lists with no dupliates

employee_numbers = []
employee_names = []
employee_salaries = []

for item in employee_data:
    # Checks for employee numbers
    if type(item) == int:
        if item not in employee_numbers:
            employee_numbers.append(item)

    # Checks for employee names
    elif type(item) == str:
        if item not in employee_names:
            employee_names.append(item)

    # Checks for employee salaries
    elif type(item) == float:
        if item not in employee_salaries:
            employee_salaries.append(item)

# Display employee information

print("Employee Numbers:")
print(employee_numbers)

print("\nEmployee Names:")
print(employee_names)

print("\nEmployee Salaries:")
print(employee_salaries)


#3 Calculate total hourly rates and add 30% for benefits

total_hourly_rates = []

for salary in employee_salaries:
    total_rate = salary + (salary * 0.30)
    total_hourly_rates.append(total_rate)

print("\nTotal Hourly Rates (including benefits):")
print(total_hourly_rates)

# 4 Checks for budget concerns

max_rate = max(total_hourly_rates)

if max_rate > 37.30:
    print("\nBudget concern: The highest total hourly rate exceeds the budget limit of $37.30.")

# 5 Find underpaid salaries

underpaid_salaries = []

for rate in total_hourly_rates:
    if 28.15 <= rate <= 30.65:
        underpaid_salaries.append(rate)

print("\nUnderpaid Salaries:")
print(underpaid_salaries)

# 6 Calculates company raises

company_raises = []

for salary in employee_salaries:
    if 22 <= salary <= 24:
        new_salary = salary * 1.05

    elif 24 < salary <= 26:
        new_salary = salary * 1.04

    elif 26 < salary <= 28:
        new_salary = salary * 1.03

    else:
        new_salary = salary * 1.02

    company_raises.append(round(new_salary, 2))

print("\nCompany Raises:")
print(company_raises)

# 7 Complex conditions with 4 truth tests

# 1. More than 5 employee numbers
# 2. More than 5 employee names
# 3. Maximum total hourly rate exceeds $30
# 4. At least 1 underpaid salary

if len(employee_numbers) > 5 and len(employee_names) > 5 and max_rate > 30 and len(underpaid_salaries) >= 1:
    print("\nCompany employee and salary data processed successfully with multiple conditions met.")