# Austin Newell
# 2-27-24
#P2LAB2
#Assignment tests student's knowledge of how to write code that displays information to users

#Get input from user
num1 = float(input('Enter a float: '))
num2 = float(input('Enter a float: '))
num3 = float(input('Enter a float: '))
num4 = float(input('Enter a float: '))

#Calculate product of variables
product = num1 * num2 * num3 * num4

#Calculate the average
average = (num1 + num2 + num3 + num4) / 4

#Display info to user
print(f'The product is: {product:.0f}')
print(f'The average is: {average:.0f}')

#Display info to user
print(f'The product is: {product:.3f}')
print(f'The average is: {average:.3f}')


