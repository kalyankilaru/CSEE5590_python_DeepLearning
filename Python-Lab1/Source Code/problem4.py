

def students(python_students, web_students):    # Function students to get common and uncommon students list

    # To print the lists
    print("\nThe list of python students: ",python_students)
    print("The list of web application students: ", web_students)

    # To print the common students list
    print("The list of students who are attending both the classes: ", end=" ")
    common_students = []    # New list for common students
    # Loop for getting the common students
    for i in python_students:
        for j in web_students:
            if i == j:
                common_students.append(i)
    print(common_students)

    # creating a new list as python students and then removing the common students
    uncommon_students = python_students
    for i in common_students:
        uncommon_students.remove(i)
    # Creating a new list and then removing the common students from it
    uncommon_students_web = web_students
    for j in common_students:
        uncommon_students_web.remove(j)
    # The list of students who are not common in both
    uncommon_students.extend(uncommon_students_web)
    print("The list of students who are not common in both the classes:", end=" ")
    print(uncommon_students)


python_students_list = ["kalyan", "chaitanya", "mahesh"]   # Python students list
web_students_list = ["kalyan", "chaitanya", "mahesh"]   # Web application students list
students(python_students_list,web_students_list)    # Calling the function by passing the lists