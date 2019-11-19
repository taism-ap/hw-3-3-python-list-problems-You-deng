# Imports the random module
import random

# Create an empty list
random_list = []

# Create 100 random numbers in a range from 0 to 99
for i in range(0,100):
 random_list.append(random.randrange(0,100))

# Print the random number list 
print (random_list)
 

# Create a function to find the minimum number in the list
def find_minimum():

  # Set m to the minimum value in the list
  m = min(random_list)

  # Print the minimum number in the list
  print (("The minimum number in this number list is ") +str((int(m))))
   

# Call the function
find_minimum()
