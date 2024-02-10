"""
create a variable to store the loop requirement
create a list that will store the numbers inputted by the user

create a while loop that continues as long as the user has not entered -1:
    create a variable that stores the value of the user input
    try to convert that value into a floating number
    if it can't convert it (ie letters):
        inform user and return to start of the loop
    if the input is not -1:
        add variable to the list
    if the input is -1:
        break out of the loop

display the list of numbers given by the user

calculate the total of these numbers and return to user
calculate the average of the total using the total value and the list length
return this value to the user
"""


loop = 0 #variable for the while loop
numbers = list() #sets up a list for number collecting

while loop == 0: #while the loop variable equals to 0
    print("-" * 50)
    num = input("Please input a number. To end, enter -1: ") #variable to collect user input
    
    try:
        num = float(num) #attempts to convert the input to a float
    except:
        ValueError #if it can't convert it to a float
        print("-" * 50)
        print("Enter a number.") #clear instruction to user
        continue #loop goes back to the start

    if num == float("-1"): #if the number is equal to a float value of -1
        loop += 1

    elif num != float("-1"): #if the number does not equal to a float value of -1
        numbers.append(num) #add the number to the list of numbers
        
print() #spacing for the next set of information

print("All numbers entered:")
for x in numbers: 
    print(x) #prints out all the numbers from the list in a column

print()

total = sum(numbers) #adds all values of the list together
print("the total value of these numbers is: ", total) #displays the total

print()

average = (total / len(numbers)) #average equals the total divided by the length of the list
print("The average of these numbers is: ", average) #displays the average

print()

print("x" * 15)
print("End of program.") #display end of program message to user
print("x" * 15)    
