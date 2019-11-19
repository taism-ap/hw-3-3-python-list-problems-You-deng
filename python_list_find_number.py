# Imports the random module
import random

# Create an empty list
random_list = []

# Create 100 random numbers in a range from 0 to 99
for i in range(0,100):
 random_list.append(random.randrange(0,100))

# Print the random number list 
print (random_list)

# Use while true statement to repeats the function forever
while True:

  # Create a function to find the times a number occurs in the list
 def find_number():

   # Set the instruction for enter the input
   x = input ("enter the number you want to know how many times it occurs in this list:")

   # Print result
   print (("this number occurs ") + str(random_list.count(int(x))) + (" times"))

 # Call the function
 find_number()
