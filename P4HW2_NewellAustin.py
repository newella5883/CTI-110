# Austin Newell
# 4/9/2024
# P4HW2
# Assignment assess student ability to edit and enhance exiting programs

name = input('Enter employee name: ')
totEmp = 0
totOT = 0
totReg = 0
totGro = 0
while name != "Done":
    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))


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
    grossPay = overtime_pay + reghour_pay
    totEmp +=1
    totOT += overtime_pay
    totReg += reghour_pay
    totGro += grossPay
    print(f"{'Employee name: ':<18} {name}")
    print()
    print(f"{'Hours Worked':<16} {'Pay Rate':<14} {'Overtime':<14} {'Overtime Pay':<17} {'RegHour Pay':<17} {'Gross Pay'}")
    print("----------------------------------------------------------------------------------------------------------")
    print(f"{hours_worked:<16} ${pay_rate:<13} {overtime:<14} ${overtime_pay:<16.2f} ${reghour_pay:<16.2f} ${(grossPay):.2f}")
    print()
    name = input('Enter employee name or "Done" to terminate: ')
print()
print('Total number of employees entered: ',totEmp)
print(f'Total amount paid for overtime: ${totOT:.2f}')
print(f'Total amount paid for regular hours: ${totReg:.2f}')
print(f'Total amount paid in gross: ${totGro:.2f}')