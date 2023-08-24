# # Importing Libraries
from mainMenu import menuFunction


print("Established Serial Connection to Arduino")
print("--------------------------------------------")

print("Welcome to the Embedded System Project")

menuFunction()


# So what is the problem now is, we are able to send data and it is taking the data and the decision but the previous functionalities arent working. 
# We know  that the serial communication is intact and everthing looks 
# good on the python side but on the main.cpp side, Im not sure, maye whats happening is 
# that we have a problem with user input 



# so basically what we know is, we are sending an signal to arduino from python, 
# when we do send decision, so it somehow is using the decision and values in main.cpp
# of rgb red green blue

# what we can do is print first, what is being received