name_list = [] #lists set up for later use
dob_list = []

print("\n","-" * 50, "\n")

with open("./DOB.txt", "r") as dob_file: #open the file and save as dob_file variable
    for line in dob_file: #for each line of text
        content = line.split(" ") #split up the line by the spaces inbetween items

        full_name = content[0] + " " + content[1] #add the first and last name together
        dob = content[2] + " " + content[3] + " " + content[4].strip() #add birthdate together
    

        name_list.append(full_name) #add the full name to a name list
        dob_list.append(dob) #add the birthdate to a date of birth list
        
print("\nName\n")
for name in name_list: #for every name in the list
    print(name) #print out the name


print("\nBirthdate\n")
for birthdate in dob_list:
    print(birthdate)    
                               

print("\n","-" * 50, "\n")









