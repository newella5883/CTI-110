#Name
#Date
#Program Detail - Input/Output

#Street is a String datatype
street = input('What is your street?')

#Convert to int() in the same line
house_num = int(input('What is your house number?'))


#Convert to int() separatly
house_num = int(house_num)

#Calculate neighbor's house number
neigh_num = house_num + 2

#Print our address and neighbor address
print('Your address is', house_num, street)

print('Your neighbor address is', neigh_num, street)
