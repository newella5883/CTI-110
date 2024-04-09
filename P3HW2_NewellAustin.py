# Austin Newell
# 3/21/2024
# P3HW2
# Assignment assess student understanding of decision structures.

name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("------------------------------------------")

if hours_worked > 40:
    overtime = hours_worked - 40
    overtime_pay = overtime * pay_rate * 1.5
    reghour = 40
    reghour_pay = reghour * pay_rate
else:
    overtime = 0
    overtime_pay = 0
    reghour = hours_worked
    reghour_pay = pay_rate * hours_worked


print(f"{'Employee name: ':<18} {name}")
print()
print(f"{'Hours Worked':<16} {'Pay Rate':<14} {'Overtime':<14} {'Overtime Pay':<17} {'RegHour Pay':<17} {'Gross Pay'}")
print("----------------------------------------------------------------------------------------------------------")
print(f"{hours_worked:<16} ${pay_rate:<13} {overtime:<14} ${overtime_pay:<16} ${reghour_pay:<16} ${(overtime_pay + reghour_pay):.2f}")





