"""
create a file called student register that can be added to
ask the user for the number of students being added to the register
for the number of students being registered:
    create an input that asks for the name of the student
    check to see that only letters have been given in the name
    add that name to the register with a dotted line next to it

"""

with open("Student Register.txt", 'a') as StudentRegister: #used 'a' instead of 'w' incase extra students need to be added later
    while True:
        
        num_students = input("\nHow many students are being registered?:  ")

        try:
            num_students = int(num_students)

        except ValueError:
            print("Please enter a number.")
            continue

        if num_students == int(num_students):
            break

    
    while num_students != 0: #for the amount of students

        
        student_first_name = input("\nPlease enter the first name of the student: ")

        student_first_name = student_first_name.capitalize()
        student_check = student_first_name.isalpha() #check to see if the name only contains letters

        if student_check == True:
            pass #continues to the next part of the process

        else:
            print("Please use only letters when entering a name.")
            continue #sends user back to the start of the name entering process


        
        student_surname = input("\nPlease enter the surname of the student:   ")

        student_surname = student_surname.capitalize()
        student_check = student_surname.isalpha()

        if student_check == True:
            pass

        else:
            print("Please use only letters when entering a name.")
            continue 

        student_name = student_first_name + " " + student_surname #full name created
        

        length = 0
        dot_alignment_limit = 50 #chose 50 in order to allow ample space for both names
        
        for x in student_name:
            length += 1

        space = dot_alignment_limit - length  

        StudentRegister.write('\n'+student_name+' '*space+'.....\n\n'+'-'*dot_alignment_limit+'\n')
        """attempted to make the document as clear as possible for the user due to potential
            overlapping of names and attendence dots within the text document"""
        
        num_students -= 1

    input("\nAll names have been added to the register, please press enter to close the program.")


    


    