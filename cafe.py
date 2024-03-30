menu = ['coffee','tea','cake','juice box']

stock = {'coffee':5,
         'tea':4,
         'cake':6,
         'juice box':2
         'latte':3
        }

price = {'coffee':3.99,
         'tea':1.99,
         'cake':3,
         'juice box':1
         'latte':4
        }


options_menu = True

while options_menu:
    print("-" * 50, "\n") #format for user-friendly environment
    print("1. Menu\n2. Stock\n3. Price\n4. Total Stock\n5. Exit")
    choice = input("\nPlease choose a number from the choices above:\n")
    print("-" * 50, "\n")

    try:
        choice = int(choice) 
    except: #if the variable can't be casted it'll ask for the user to input again
        ValueError
        print("Please enter a number.")
        continue
    
    if choice == 1:
        
        print("The current items on the menu in Super Coffee are:")

        for item in menu:
            print(item)

        print("\nThese are the current products available.")
        input("Press enter to return to the options screen.") #allows user to read data before going back to the menu
        

    elif choice == 2:
        
        print("The amount of stock for the menu are:")

        for item in menu:
            print(item +":",stock.get(item))

        input("Press enter to return to the options screen.") 


    elif choice == 3:
        
        print("The current price for the items in the menu are:")

        for item in menu:
            print(item +":",price.get(item))

        input("Press enter to return to the options screen.")
    
    elif choice == 4:
        cafe_value = []
        total_cafe_value = 0

        for item in menu:
            total_stock = (stock.get(item) * price.get(item))
            cafe_value.append(total_stock)
            print("{}: £{}".format(item,round(total_stock, 2))) #prints out item and its current stock pound value

        for value in cafe_value:
            total_cafe_value += value #adds up all the values for a grand total

        print("The total value of stock in the cafe is £{}".format(round(total_cafe_value,2)))
        input("Press enter to return to the options screen.")
             

    elif choice == 5:
        options_menu = False #breaks out of the menu loop

    

    
