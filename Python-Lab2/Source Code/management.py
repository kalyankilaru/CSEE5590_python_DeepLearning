
class System(object):

    # student id is initially assigned to 1 and is incremented when ever a new student is added
    id_student = 1

    # The initialize constructor is defined where the initial values are assigned
    def __init__(self, name, age, sec):
        System.id_student += 1
        self.name = name    # initializing name
        self.age = age      # initializing age of a student
        self.sec = sec      # initializing sec of a student

    # student info function is used to display the details of the students and give the student an id
    def studentinfo(self):
        print("Student Information : " + self.name + " age is " + str(
            self.age) + " and admitted in the section " + self.sec + " where the student ID assigned is:  " + str(System.id_student))

    # The below is the student class which inherits the system class

class Student(System):

    def __init__(self, name, age, sec):
        # The super method calls the parent class constructor
        super(Student, self).__init__(name, age, sec)

    def studentinfo(self):
        print("studentinfo method in student class is invoked")

    # This medthod prints the class name
    
    def classidentity(self):
        print("Student Class method")

    # Student sport method tells you which sport student plays
    
    def studentsport(self):
        print("Student is interested in: " + self.game)

    # Only the student object can have an access to this private member
    def __idnum(self):
        print("Private data member")


    # Student is parent class which is inherited by the grades class
    
class Grades(Student):
    # The constructor which takes  various courses as input and initialize them
   
    def __init__(self, english, hindi, telugu):
        self.english = english
        self.hindi = hindi
        self.telugu = telugu

    # This method displays the scpre of the students in each course
    def score(self):
        print(
            "Student got good score, with" + self.english + " grade in english, " + self.hindi + " grade in hindi and " + self.telugu + " grade in telugu ")

    def studentinfo(self):
        print("Grade class")

    # The final score of the student is defined here
    def finalscore(self):
        print("Student graduated with good grade")


# Class enroll that extends the student and system class. so that the subclass can access the parents class methods

class Enroll(Student, System):
    
    # the constructor that takes the initial values 
    def __init__(self, name, age, sec):
        # Super which call the parent constructor
        super(Enroll, self).__init__(name, age, sec)


# studentsports class extends the student class
class studentsports(Student):

    def __init__(self, game):
        self.game = game


# Class grade that inherits different classes

class grad(Student, System):
    # The initialize constructor
    
    def __init__(self, name, degree):
        self.degree = degree
        self.name = name

    def studentdetails(self):
        print(self.name + " is graduated in" + self.degree)


# object creation
name = input("Enter student name: ")
age = int(input("Enter student age: "))
sec = input("Enter student sec: ")

systema = System(name, age, sec)

systema.studentinfo()

sa = Student(name, age, sec)

sa.studentinfo()
sb = Student(name, age, sec)
sc = Student(name, age, sec)

gradea = Grades('B', 'X+', 'X')

gradea.score()
enrolla = Enroll('kalyan', 26, 'Fresher')
enrolla.studentinfo()
sportsa = studentsports('Football')
sportsa.studentsport()
sa._Student__idnum()
gs = grad('kalyan', 'Economics')
gs.studentdetails()