# Imports the random module
import random

# Create an empty list
random_list = []

# Create 100 random numbers in a range from 0 to 99
for i in range(0,100):
 random_list.append(random.randrange(0,100))

# Print the random number list 
print (random_list)
 

# Create a function to find the maximum number in the list
def find_maximum():

  # Set m to the maximum value in the list
  m = max(random_list)

  # Print the maximum number in the list
  print (("The maximum number in this number list is ") +str((int(m))))
   

# Call the function
find_maximum()
