import sys
print("This is to be used before each show to")
print("calculate an estimate of the efficiency of the team.")
print("(Disclosure: This does not consider motivation/capability/willpower")
print("or any other personal trait, this program is to determine the need")
print("of the execution of a failsafe or back-up plan: >75% = Safe.)")
def Menu():
    global a1
    global a2
    global a3
    global a4
    global a5
    global Total
    global Final
    choice = True
    print("-" * 40)
    if a1 == True:
        print("Option 1: Sound System / Lighting / Stage")      #All departments in a menu setting                            
    if a2 == True:
        print("Option 2: Performers")
    if a3 == True:
        print("Option 3: Catering")
    if a4 == True:
        print("Option 4: Venue / Security")
    if a5 == True:
        print("Option 5: Promoters")
    if Final == 0:
        print("Option T: Total Efficiency")
    print("Option Q: Quit Program")
    print("-" * 30)
    while choice == True:                                                           
        Decision = input("Enter one of the above options:   ")                    
        if Decision == "1":                                      
            if a1 == True:
                Run1()                                                                  
                choice = False
            elif a1 == False:
                print("(Error: Can't access same area twice)")
                choice = True
        elif Decision == "2":                                    
            if a2 == True:
                Run2()                                                                  
                choice = False
            elif a2 == False:
                print("(Error: Can't access same area twice)")
                choice = True
        elif Decision == "3":    
            if a3 == True:
                Run3()                                                                  
                choice = False
            elif a3 == False:
                print("(Error: Can't access same area twice)")
                choice = True
        elif Decision == "4":
            if a4 == True:
                Run4()                                                                  
                choice = False
            elif a4 == False:
                print("(Error: Can't access same area twice)")
                choice = True
        elif Decision == "5":
            if a5 == True:
                Run5()                                                                  
                choice = False
            elif a5 == False:
                print("(Error: Can't access same area twice)")
                choice = True
        elif Decision == "Q" or Decision == "q":
            RunQ()
            choice = False
        elif Decision == "T" or Decision == "t":
            if Final == 0:
                print("-" * 40)
                print(Total, "% Total Efficiency")          #Efficiency of all departments
                print("")
                print(g1, "% From Sound System / Lighting / Stage")
                print(g2, "% From Performers")
                print(g3, "% From Catering")
                print(g4, "% From Venue / Security")
                print(g5, "% From Promoters")

                if Total <= 75:
                    print("-" * 40)
                    print("WARNING: EFFICIENCY LEVELS ARE TOO LOW FOR OPTIMAL PERFORMANCE")
                
                else:
                    print("-" * 40)
                    print("Optimal Levels Attained")
                
                print("-" * 40)
                choice = False

            elif Final != 0:
                print("(Access Denied)")
                choice = True
            
        else:
            choice = True
    
    
def Run1():
    department = 0
    print("-" * 40)
    print("Sound System / Lighting / Stage")
    global Total                                            
    global Sub
    global g1
    global a1
    global Final
    loop = True
    V_1 = []                                        #Local Variable defined as Empty
    V_2 = []
    V_3 = []
    V_4 = []
    
    while loop == True:
        V_1 = input("Are all members of this group present? Y/N:    ")
        if V_1 == "Y" or V_1 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_1 == "N" or V_1 == "n":
            loop = False
        else:
            loop = True
            
    loop = True
    while loop == True:
        V_2 = input("Have all tasks been acomplished? Y/N:   ")
        if V_2 == "Y" or V_2 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_2 == "N" or V_2 == "n":
            loop = False
        else:
            loop = True
    

    
    
    loop = True
    while loop == True:
        V_3 = input("Have back-up plans been made? Y/N   ")
        if V_3 == "Y" or V_3 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_3 == "N" or V_3 == "n":
            loop = False
        else:
            loop = True
    

    
    
    loop = True
    while loop == True:
        V_4 = input("Have you been informed of what other areas are doing? Y/N   ")
        if V_4 == "Y" or V_4 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_4 == "N" or V_4 == "n":
            loop = False
        else:
            loop = True

    a1 = False
    Final -= 1
    g1 += department
    print(department, "% efficiency in this area.")
    input("(Press Enter to Continue)")
    Menu()

                
    

def Run2():
    department = 0
    print("-" * 40)
    print("Performers")
    global Total
    global Sub
    global g2
    global a2
    global Final
    loop = True
    V_1 = []                                        
    V_2 = []
    V_3 = []
    V_4 = []
    
    while loop == True:
        V_1 = input("Are all members of this group present? Y/N:    ")
        if V_1 == "Y" or V_1 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_1 == "N" or V_1 == "n":
            loop = False
        else:
            loop = True
            
    loop = True
    while loop == True:
        V_2 = input("Have all tasks been acomplished? Y/N:   ")
        if V_2 == "Y" or V_2 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_2 == "N" or V_2 == "n":
            loop = False
        else:
            loop = True
    

    
    
    loop = True
    while loop == True:
        V_3 = input("Have back-up plans been made? Y/N   ")
        if V_3 == "Y" or V_3 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_3 == "N" or V_3 == "n":
            loop = False
        else:
            loop = True
    

    
    
    loop = True
    while loop == True:
        V_4 = input("Have you been informed of what other areas are doing? Y/N   ")
        if V_4 == "Y" or V_4 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_4 == "N" or V_4 == "n":
            loop = False
        else:
            loop = True

    a2 = False
    Final -= 1
    g2 += department
    print(department, "% efficiency in this area.")
    input("(Press Enter to Continue)")
    Menu()


def Run3():
    department = 0
    print("-" * 40)
    print("Catering")
    global Total
    global Sub
    global g3
    global a3
    global Final
    loop = True
    V_1 = []                                        
    V_2 = []
    V_3 = []
    V_4 = []
    
    while loop == True:
        V_1 = input("Are all members of this group present? Y/N:    ")
        if V_1 == "Y" or V_1 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_1 == "N" or V_1 == "n":
            loop = False
        else:
            loop = True
            
    loop = True
    while loop == True:
        V_2 = input("Have all tasks been acomplished? Y/N:   ")
        if V_2 == "Y" or V_2 == "y":
            Total += Sub
            loop = False
            
        elif V_2 == "N" or V_2 == "n":
            loop = False
        else:
            loop = True
    

    
    
    loop = True
    while loop == True:
        V_3 = input("Have back-up plans been made? Y/N   ")
        if V_3 == "Y" or V_3 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_3 == "N" or V_3 == "n":
            loop = False
        else:
            loop = True
    

    
    
    loop = True
    while loop == True:
        V_4 = input("Have you been informed of what other areas are doing? Y/N   ")
        if V_4 == "Y" or V_4 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_4 == "N" or V_4 == "n":
            loop = False
        else:
            loop = True

    a3 = False
    Final -= 1
    g3 += department
    print(department, "% efficiency in this area.")
    input("(Press Enter to Continue)")
    Menu()


def Run4():
    department = 0
    print("-" * 40)
    print("Venue / Security")
    global Total
    global Sub
    global g4
    global a4
    global Final
    loop = True
    V_1 = []                                        
    V_2 = []
    V_3 = []
    V_4 = []
    
    while loop == True:
        V_1 = input("Are all members of this group present? Y/N:    ")
        if V_1 == "Y" or V_1 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_1 == "N" or V_1 == "n":
            loop = False
        else:
            loop = True
            
    loop = True
    while loop == True:
        V_2 = input("Have all tasks been acomplished? Y/N:   ")
        if V_2 == "Y" or V_2 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_2 == "N" or V_2 == "n":
            loop = False
        else:
            loop = True
    

    
    
    loop = True
    while loop == True:
        V_3 = input("Have back-up plans been made? Y/N   ")
        if V_3 == "Y" or V_3 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_3 == "N" or V_3 == "n":
            loop = False
        else:
            loop = True
    

    
    
    loop = True
    while loop == True:
        V_4 = input("Have you been informed of what other areas are doing? Y/N   ")
        if V_4 == "Y" or V_4 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_4 == "N" or V_4 == "n":
            loop = False
        else:
            loop = True

    a4 = False
    Final -= 1
    g4 += department
    print(department, "% efficiency in this area.")
    input("(Press Enter to Continue)")
    Menu()

def Run5():
    department = 0
    print("-" * 40)
    print("Promoters")
    global Total
    global Sub
    global g5
    global a5
    global Final
    loop = True
    V_1 = []                                        
    V_2 = []
    V_3 = []
    V_4 = []
    
    while loop == True:
        V_1 = input("Are all members of this group present? Y/N:    ")
        if V_1 == "Y" or V_1 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_1 == "N" or V_1 == "n":
            loop = False
        else:
            loop = True
            
    loop = True
    while loop == True:
        V_2 = input("Have all tasks been acomplished? Y/N:   ")
        if V_2 == "Y" or V_2 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_2 == "N" or V_2 == "n":
            loop = False
        else:
            loop = True
    

    
    
    loop = True
    while loop == True:
        V_3 = input("Have back-up plans been made? Y/N   ")
        if V_3 == "Y" or V_3 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_3 == "N" or V_3 == "n":
            loop = False
        else:
            loop = True
    

    
    
    loop = True
    while loop == True:
        V_4 = input("Have you been informed of what other areas are doing? Y/N   ")
        if V_4 == "Y" or V_4 == "y":
            Total += Sub
            department += 5
            loop = False
            
        elif V_4 == "N" or V_4 == "n":
            loop = False
        else:
            loop = True

    a5 = False
    Final -= 1
    g5 += department
    print(department, "% efficiency in this area.")
    input("(Press Enter to Continue)")
    Menu()



def RunQ():
    exit(sys)
    






Sub = 5
Total = 0

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

a1 = True
a2 = True
a3 = True
a4 = True
a5 = True

Final = 5

Menu()
