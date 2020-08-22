# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with handling exceptions and understanding pickling
#               in Python
# ChangeLog (Who,When,What):
# RebeccaLy, 08.19.20, Created script
# ---------------------------------------------------------------------------- #

# Try/Except Block for ValueError Exception
try:
    name = input("What is your name? ") # Asks user for name to be input
    age = int(input("how old are you? ")) # Converts user input to an int
except ValueError as e:
    print("Age needs to be a number only, please try again") # Prints message
    print(e) # Prints python error message for ValueError
else:
    print("Your name is " + name + " and your age is " + str(age) + ".\n") # Prints custom message

# Pickling Example
import pickle # imports pickle module
doctors = ['Christopher Eccleston', 'David Tennant', 'Matt Smith', 'Peter Capaldi'] # Loads into a list called 'doctors'
with open ('doctorWho.dat', 'wb') as file: # opens file with write mode
    pickle.dump(doctors, file) # Dumps the 'doctor' list into the file
    print("Your file has been pickled! \n") # Prints confirmation message to the user

#Unpickling list from doctorWho.txt file
unpack_doctors = open('doctorWho.dat', 'rb') # Opens file with the read mode to the byte file
names = pickle.load(unpack_doctors) # Loads the list back out from the file
print('Here is your data unpickled!') # Prints confirmation message to the user
print(names) # Prints the list back out 

