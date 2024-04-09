# Austin Newell
# 02-26-24
# P1HW2
# Assignment requires using IDLE to create and test a program.

#Ask user to enter their budget
#Ask user to enter travel destination
#Ask user for amount they will spend on gas
#Ask user for amount they will spend on accommodation
#Ask user for amount they will spend on food
#Add expenses
#Subtract expenses from budget
#Display results

budget = float(input('Enter budget here:'))
destination = input('Enter destination:')
gas = float(input('Enter gas here:'))
hotel = float(input('Enter hotel here:'))
food = float(input('Enter food here:'))
print()

print('This program calculates and displays travel expenses')
print()
print('Enter budget here: ', budget)
print()
print('Enter destination here: ', destination)
print()
print('Enter gas here: ', gas)
print()
print('Enter hotel here: ', hotel)
print()
print('Enter food here: ', food)
print()

print('------------Travel Expenses------------')
print('Location: ', destination)
print('Intital Budget: ', budget)
print()
print('Fuel:', gas)
print('Accomodation: ', hotel)
print('Food: ', food)
print()

print('Remaining Balance: ', budget - gas - hotel - food)

