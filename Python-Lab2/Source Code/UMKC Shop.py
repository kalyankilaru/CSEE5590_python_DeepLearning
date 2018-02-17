
# The books dictionary with book name and the cost of the book
books = {"python 3":45,"OOPS":35,"Electronics":25,"Advanced Maths":65,"Food Guide":30}
print("\n")
print(books)    # For printing the books

# To get the range from the user
minimum_cost = int(input("Enter the minimum cost to search the available books: "))
maximum_cost = int(input("Enter the maximum cost to search the available books: "))

print("The available books with in the range are: ")
# The available books within the range are displayed.
count = 0
for key in books:
    if books[key] >= minimum_cost and  books[key] <=  maximum_cost:
        count = 1
        print(key)
if count == 0:
    print("Sorry! There are no books available with in the range")