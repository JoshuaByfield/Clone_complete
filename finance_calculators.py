
#this program uses step_1 - step_4 variables in while loops 
#in order to easily see where each user input is required for further progression.
import math

#Below is a variable list that determines the initial while loop as well as the potential choices
menu = 0 
invest = 0
bond = 0
print()

while menu == 0:
    print("-" * 50) #format for readability
    choice = input("Please select either Investment or Bond: ").lower() #automatically lowers the input
    print("-" * 50)
    if choice == "investment":
        invest = 1 #activates investment loop
        menu = 1 #gets out of the initial menu

    elif choice == "bond":
        bond = 1 #acivates bond loop
        menu = 1 #gets out of the initial menu
    
    else:
        print("Please only choose between Investment or Bond.")

if invest == 1:
    print("You have selected investment")
    while invest == 1:

        step_1 = 1
        while step_1 == 1:
            print("-" * 50)
            amount = input("How much money are you depositing?: £")
            print("-" * 50)
            try:
                amount = int(amount)

            except ValueError: #when it doesn't equal the integer data type
                print("Please enter a number.")
                continue #repeats the  current loop from the start

            if amount == int(amount):
                print()
                step_1 -= 1
        
        step_2 = 1
        while step_2 == 1:     
            print("-" * 50)     
            interest_rate = input("What is the number of interest rate?: ")
            print("-" * 50)

            try:
                interest_rate = int(interest_rate)

            except ValueError:
                print("Please enter a number.")
                continue
            
            if interest_rate == int(interest_rate):
                print()
                step_2 -= 1

        step_3 = 1   
        while step_3 == 1:
            print("-" * 50)
            years = input("How many years are you planning to invest?: ")
            print("-" * 50)
            try:
                years = int(years)

            except ValueError:
                print("Please enter a number.")
                continue

            if years == int(years):
                step_3 -= 1


        
        #Below calculation variables 
        r = (interest_rate / 100)
        p = amount
        t = years

        calculations = 1

        while calculations == 1:
            
            print("-" * 50)
            interest = input("Simple or Compound interest?: ").lower()
            print("-" * 50)
        
            if interest == "simple":
                final_value = p *(1 + r*t) #simple interest calculation
                print()
                print("-" * 50)
                print("£{} simple interest over {} years.".format(round(final_value, 2), years)) #formats and rounds the variables to currency
                print("-" * 50)

                invest -= 1
                calculations -= 1
                

            elif interest == "compound":
                final_value = p * math.pow((1+r),t) #compound interest calculation
                print()
                print("-" * 50)
                print("£{} compounded interest over {} years.".format(round(final_value, 2), years))
                print("-" * 50)

                invest -= 1
                calculations -= 1
                

            elif (interest != "simple") or (interest != "compound"):
                print("Please enter 'Simple' or 'Compound'.")



elif bond == 1:
    print("you have selected bond.")
    step_1 = 1
    while step_1 == 1:
        print("-" * 50)
        house = input("What is the current value of your house?: £")
        print("-" * 50)

        try:
            house = int(house)
        except:
            ValueError
            print("Please enter a number.")
            continue

        if house == int(house):
            print()
            step_1 -= 1
    
    step_2 = 1
    while step_2 == 1:
        print("-" * 50)
        interest_rate = input("What is the interest rate?: ")
        print("-" * 50)
        try:
            interest_rate = int(interest_rate)
        except:
            ValueError
            print("Please enter a number.")
            continue

        if interest_rate == int(interest_rate):
            print()
            step_2 -= 1

    step_3 = 1
    while step_3 == 1:
        print("-" * 50)
        months = input("How many months are you planning to take to repay the bond?: ")
        print("-" * 50)
        try:
            months = int(months)
        except:
            ValueError
            print("Please enter a number.")
            continue
        if months == int(months):
            print()
            step_3 -= 1
        
        p = house
        i = (interest_rate / 100)
        n = months

        repayment = (i * p)/(1 -(1 + i)**(-n)) #bond calculation

        print()
        print("-" * 50)
        print("you will need to pay £{} per month for {} months in order to repay the bond.".format(round(repayment, 2),months))
        print("-" * 50)




        
print("End of program.")
