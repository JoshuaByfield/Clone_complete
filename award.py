"""
create an input variable to store the users swimming time in minutes
if this input can not be converted into an integer then ask them to input their time again

create an input variable to store the users cycling time in minutes
if this input can not be converted into an integer then ask them to input their time again

create an input variable to store the users running time in minutes
if this input can not be converted into an integer then ask them to input their time again

create a variable that adds up all the previously input times into one time

return to the user all the times they input
return to the user the total time.

if the total is greater than or equal to 0 and less than or equal to 100
    award the Provincial Colours
if the total is greater than or equal to 101 and less than or equal to 105
    award the Provincial Half Colours
if the total is greater than or equal to 106 and less than or equal to 110
    award the Provincial Scroll
if the total is greater than 110
    no award to be given

"""
#Below are used for the while loops
check_1 = 0
check_2 = 0
check_3 = 0

print()
print("-" * 50) #neatens for readability
print("Please enter all times in minutes. No seconds will be counted.") #displays instructions for the user
print("-" * 50)
print()

#while loops for user to input their times
while check_1 == 0:
    print("-" * 50)
    swimming_time = input("Please enter your swimming time: ") #variable asking for the user to input their time
    print("-" * 50)
    try:
        swimming_time = int(swimming_time) #attempts to convert the input string into an integer
    except ValueError: #if the attempt to convert doesn't work
        check_1 = 0
        print("Please enter a valid time.")
    else:
        check_1 = 1

while check_2 == 0:
    print("-" * 50)
    cycling_time = input("Please enter your cycling time: ")
    print("-" * 50)
    try:
        cycling_time = int(cycling_time)
    except ValueError:
        check_2 = 0
        print("Please enter a valid time.")
    else:
        check_2 = 1

while check_3 == 0:
    print("-" * 50)
    running_time = input("Please enter your running time: ")
    print("-" * 50)
    try:
        running_time = int(running_time) 
    except ValueError: 
        check_3 = 0
        print("Please enter a valid time.")
    else:
        check_3 = 1 

total = swimming_time + cycling_time + running_time #adds up all the times into one variable

#Below displays the individual times as well as the grand total
print()
print("-" * 50)
print("Your times were {} minutes for swimming, {} minutes for cycling, and {} minutes for running.".format(swimming_time, cycling_time, running_time))
print("Your total time to complete the triathlon in minutes was: {}".format(total))
print("-" * 50)
print()

#Below determines the award based on the ranges of 0-100, 101-105, 105-110, and over 110
if total >= 0 and total <= 100: #if total is greater than or equal to 0 and total is less than or equal to 100
    print("You've been awarded Provincial Colours, well done!")
elif total >= 101 and total <= 105:
    print("You've been awarded Provincial Half Colours, well done!")
elif total >= 106 and total <= 110:
    print("You've been awarded Provincial Scroll, well done!")
elif total >= 111:
    print("Unfortunately you do not receive an award based on your time. Well done for participating!")