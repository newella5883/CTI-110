# Austin Newell
# 3-4-24
# P2HW1
# Assignment assess student ability to edit and enhance exiting programs

budget = float(input('Enter budget here:'))
destination = input('Enter destination:')
gas = float(input('Enter gas here:'))
hotel = float(input('Enter hotel here:'))
food = float(input('Enter food here:'))
print()

print('This program calculates and displays travel expenses')
print()
print('Enter budget: ', budget)
print()
print('Enter your travel destination: ', destination)
print()
print('How much do you think you will spend on gas?: ', gas)
print()
print('Approximately, how much will you need for accomodation/hotel?: ', hotel)
print()
print('Last, how much do you need for food?: ', food)
print()

print('------------Travel Expenses------------')
print(f"{'Location: ':<18} {destination}")
print(f"{'Intital Budget: ':<18} ${budget:.2f}")
print(f"{'Fuel:' :<18} ${gas:.2f}")
print(f"{'Accomodation: ':<18} ${hotel:.2f}")
print(f"{'Food: ':<18} ${food}")
print('----------------------------------------')
print()
print(f"{'Remaining Balance: ':<18} ${budget - gas - hotel - food:.2f}")



