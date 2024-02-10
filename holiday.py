
def break_line(num=80):     #Format function for less repetition in code
    print("\n", "-"*num, "\n")

def enter():        #'Press enter' function for less repetition in code
    input("Press enter to continue.")

city_list = {
    "Rome":150,
    "London":100,
    "New York":250,
    "Atlantis":500
    }


while True:
    while True:     #User determines destination
        break_line()

        print("\nCity Flights Available\n")
        for location in city_list:
            print(location)

        print()
        break_line()
        city_flight = input("Please enter the desired location: ")
        city_flight = city_flight.title()

        if city_flight in city_list:
            print(f"\nYou have chosen: {city_flight}.")
            enter()
            break
        
        elif city_flight not in city_list:
            print("\nPlease enter a valid Location.")
            enter()
            

    while True:     #User determines nights stayed
        break_line()

        num_nights = input("\nHow many nights will you be staying?:   ")

        if num_nights.isnumeric():
            num_nights = int(num_nights)
            print(f"\nyou have entered {num_nights} nights.")
            enter()
            break
        
        else:
            print("Please enter a number.")
            enter()


    while True:     #User determines car hire days
        break_line()

        rental_days = input("How many days will you hire a car?:    ")

        if rental_days.isnumeric():
            rental_days = int(rental_days)
            print(f"You are hiring a car for {rental_days} days.")
            enter()
            break
        
        else:
            print("Please enter a number.")
            enter()

  
    def hotel_cost(cost):       #Calculate hotel cost
        hotel_price = num_nights*cost
        return hotel_price

    def plane_cost(location):       #Calculate plane/flight cost
        if location in city_list:
            plane_price = city_list.get(location)
            return plane_price
        
    def car_rental(cost):       #Calculate car hire cost
        car_price = rental_days*cost
        return car_price

    def holiday_cost():     #Calculate total cost and display info table
        total_cost = (hotel_price
        + plane_price
        + car_price)
        break_line()

        print( f"Plan:{city_flight}          Price"
              , "\n----------------------------------"
              , f"\nHotel:        |    £{hotel_price}"
              , f"\nPlane:        |    £{plane_price}"
              , f"\nCar:          |    £{car_price}"
              , f"\nTotal Cost:   |    £{total_cost}"
              , "\n----------------------------------")
        enter()
        break_line()
        

    hotel_price = hotel_cost(100)
    plane_price = plane_cost(city_flight)
    car_price = car_rental(40)
    holiday_cost()

    repeat_program = input("Not happy with your choice?\n"+
                    "If you would like to repeat the program, press enter.\n"+
                    "If you'd like to end the program, enter 'QUIT'.\n")
    
    repeat_program = repeat_program.upper()
    
    if repeat_program == 'QUIT':
        break

    else:
        continue
    
        

