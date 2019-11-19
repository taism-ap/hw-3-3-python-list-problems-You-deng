# Imports the random module
import random

# Create an empty list
random_list = []

# Create 100 random numbers in a range from 0 to 99
for i in range(0,100):
 random_list.append(random.randrange(0,100))

# Print the random number list 
print (random_list)

# Create a function to sort the list in ascending order
def sort():

 # Sort the list in ascending order
 random_list.sort()

 # Print the sorted list
 print (random_list)

# Call the function
sort()
