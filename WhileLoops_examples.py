#While loop - run until a specific condition is met

run_again = 'yes'

#Create incrementer variable

#add values to this cariable
my_num = 0
#How many times the loop executes
num_loops = 0

while run_again != "no":
    #iNCREMENT num_loops
    num_loops += 1

    integer = int(input("Gimme a number: "))
    my_num += integer

    #Control the loop - without it, its in infinite loop
    run_again = input("Would you like to run again?")

#Break the loop
print(f"The loop ran {num_loops}times")
print(f"The sum of the values is {my_num}")