
    # Function to perforn the operations


def contacts_list():
        contacts = [{"Name": "kalyan", "Number": 8167459970, "MailId": "005kvs@gmail.com"},     # Contact list
                    {"Name": "chaitanya", "Number": 8161234569, "MailId": "cpk@yahoo.com"},
                    {"Name": "vinod", "Number": 9176435678, "MailId": "vinodM@linkdin.com"}]

        print("1. Display Contact details by name")         # To print the details of the operations performed
        print("2. Display contact details by number")
        print("3. Edit the contact number by name")
        print("4. Exit")
        operation = int(input("Enter the numbers from 1 to 4 to perform the above operations: "))   # user selected operation

        search = 0
        # To search for a name and display the contact details
        if operation == 1:
            search_name = (input("please enter the name to search the contact: "))
            for contact in contacts:            # For loop to retrieve through the dictionary
                if search_name in contact.values():
                    search = 1
                    print(contact)
                    break
            if search == 0:
                print("Contact not found in the contact list")
                exit(0)

        # To search for a number and get the contact details
        elif operation == 2:
            search_number = int(input("Enter the number to search for the contact details:"))
            for contact in contacts:            # For loop to retrieve through the dictionary
                if contact["Number"] == search_number:
                    search = 1
                    print(contact)
                    break
            if search == 0:
                print("Contact not found in the contact list")
                exit(0)

        # To search for the name and edit the number
        elif operation == 3:
            edit_name = str(input("Enter the contact name to edit the contact number: "))
            for contact in contacts:        # For loop to retrieve through the dictionary
                if contact["Name"] == edit_name:
                    search = 1
                    print(contact)
                    edit_number = int (input("Enter the new number to update: "))
                    contact["Number"] = edit_number         # Give the new number
                    print("The contact details have been updated: ")
                    print(contact)
                    break
            if search == 0:
                print("Contact name not found on the contact list")
                exit(0)
        # If the user want to exit
        elif operation == 4:
            print("Thanks for using the application.")
            exit(0)

        else:   # If the user entered a wrong operation
            print("Wrong input! Run it again :)")


contacts_list()