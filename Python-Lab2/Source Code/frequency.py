
# We are importing the numpy as nmp
import numpy as nmp

# We are initializing the vector with 15 random numbers from 0 to 20
vector = nmp.random.randint(0,20, size=15)
# To print the generated array
print("Randomly generated array:",end=" ")
print(vector)   # to print the random array
frequent_number = nmp.bincount(vector)          # We will get the count of each random number
print("The number that appeared more frequently is: ")        # The random number which occurs maximum times
print(nmp.argmax(frequent_number))          # To print the more frequent random number