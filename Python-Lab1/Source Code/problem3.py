
# The function where the list is passed and it will find the triplets
def triplets(number_list):

    # Finding the length of the list
    total_digits = len(number_list)
    # To print the input the output
    print("\nThe list of numbers are: ", number_list)
    print("The Triplets from the list whose sum is zero are: ", end=" ")
    # As we are taking 3 numbers from the list we take the range from starting till last but 2
    for i in range(0,total_digits-2):
        # As this is the second loop we take all except the last value in the list
        for j in range (i+1,total_digits-1):
            # We take till the end of the list in this loop starting from third element
            for k in range (j+1,total_digits):
                # Checking if the triplets give the sum equal to Zero
                if number_list[i] + number_list[j] + number_list[k] == 0:
                    print("[(",number_list[i], ",", number_list[j],",", number_list[k],")]")


number_list = [1, 1, -2, 0, -1, 2, 8, -2, 9]      # The list which consists of numbers
triplets(number_list)   # Calling the function by passing the list
