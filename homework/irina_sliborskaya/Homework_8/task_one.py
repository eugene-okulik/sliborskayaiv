import random


def calculate_income():
    salary = int(input("Enter your salary: "))
    bonus_applied = random.choice([True, False])
    bonus = random.randint(1, 9000)

    if bonus_applied:
        income = salary + bonus
    else:
        income = salary

    print(f"{salary}, {bonus_applied} - '${income}'")


calculate_income()
