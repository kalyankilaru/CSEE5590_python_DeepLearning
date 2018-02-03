
# Function to check for the criteria
def passwordvalidation():

    validation = 0  # Assigning the value to validation so that to check if no error at the end

    # while loop to iterate for entering the password if it does not met the criteria
    while validation == 0:
        password = input("\nEnter your UMKC Application password: ")
        password_length = len(password)   # To get the length

        validation = 1
        # Checking the length criteria of the password entered
        if password_length < 6 or password_length > 16:
            validation = 0
            # To print the text that the password  is missing
            print("The password length should be in range 6-16 characters")

        digit = 0
        # Checking if a digit is present in the password
        for i in password:
            if i.isnumeric():
                digit = 1
                break
        if digit == 0:
            validation = 0
            print("The password should have atleast one number")    # To print the text that the password  is missing

        specialcharacter = 0
        # To check for the special characters
        for i in password:
            if i == "$" or i == "@" or i == "!" or i == "*":
                specialcharacter = 1
                break
        if specialcharacter == 0:
            validation = 0
            # To print the text that the password  is missing
            print("Password should have atleast one special character in [$@!*]")

        lowerCase = 0;
        # To check if the password contains lower case letters
        for i in password:
            if i.islower():
                lowerCase = 1
                break
        if lowerCase == 0:
            validation = 0
            # To print the text that the password  is missing
            print("Password should have atleast one lowercase character")

        upperCase = 0
        # To check if the password contains upper case letters
        for i in password:
            if i.isupper():
                upperCase = 1
                break
        if upperCase == 0:
            validation = 0
            # To print the text that the password  is missing
            print("Password should have atleast one uppercase character")
    # If the password met the criteria we will be out of the loop and print the following message
    if validation == 1:
        print("Your password met the criteria !")
passwordvalidation()    # Function to be called to verify the password



