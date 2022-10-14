"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""
import datetime
from datetime import date, datetime, timedelta


class Student:
    num_of_students = 0

    def __init__(self, f_name, s_name, dob_ddmmyy, id):
        self.f_name = f_name
        self.s_name = s_name
        self.dob_ddmmyy = dob_ddmmyy
        self.id = id
        self.subjects = dict()

        Student.num_of_students += 1

    def fullname(self):
        return "{} {}".format(self.f_name, self.s_name)

    # Display_student method displays all data for student.
    def display_student(self):
        print("Student details:")
        print("Name: {}".format(Student.fullname(self)))
        print("Date of Birth: {}".format(self.dob_ddmmyy))

    def date_today(self):
        return date.today().strftime("%d%m%y")

    def display_date_today(self):
        today = self.date_today()
        print("Date: ", today)

# I cant get this to work! Help would be appreaciated
    def find_age(self):
        birth_date = datetime.strptime(self.dob_ddmmyy, "%Y%m%d")
        format_birth_date = (datetime.strftime(birth_date, "%Y%m%d"))
        today = date.today()
        today_formatted = (datetime.strftime(today, "%Y%m%d"))
        days_in_year = 365.2425
        print(format_birth_date)
        print(date.today())
        age = (today_formatted - format_birth_date) // timedelta(days_in_year)
        print(age)
        # print("Age: {} years".format(age))









# CREATING INSTANCES
# student_1 = Student("Emma", "Gill", "100373", 1)
# student_2 = Student("Ian", "Dawson", "130670", 2)

# TRYING METHODS
# print(student_1.fullname())
# print(Student.num_of_students)
# print(Student.display_student(student_1))

class CFGStudent(Student):

    def __init__(self, f_name, s_name, dob_ddmmyy, id, cfg_courses=None):
        super().__init__(f_name, s_name, dob_ddmmyy, id)
        if cfg_courses is None:
            self.cfg_courses = []
        else:
            self.cfg_courses = cfg_courses
        self.markbook = {}

    def view_subjects(self):

        if not self.cfg_courses:
            print("Student not registered for any courses")
        elif len(self.cfg_courses) > 0:
            print("{} CFG Courses:".format(self.fullname()))
            for course in self.cfg_courses:
                print("--", course)
        else:
            return "Error"

    # NEXT STEPS: make it possible to input multiple courses at once
    def add_courses(self, course):
        if course not in self.cfg_courses:
            self.cfg_courses.append(course)

    # NEXT STEPS: make it possible to remove multiple courses at once
    def remove_courses(self, course):
        if course in self.cfg_courses:
            self.cfg_courses.remove(course)

    # USER INPUT to MARKBOOK
    def input_add_markbook(self):
        assignment = input("assignment name: ")
        try:
            grade = int(input("Grade: "))
        except:
            print("Error! please enter a number")
            quit()
        self.markbook[assignment] = grade

    # ARGUMENT INPUT to MARKBOOK
    def add_markbook(self, assignment, grade):
        if grade is int or float and grade > 0:
            try:
                grade = int(grade)
            except:
                print("Error! markbook only accepts whole numbers")
                exit()
            self.markbook[assignment] = grade
        else:
            print("Error! markbook only accepts whole numbers")
            exit()

# ARGUMENT INPUT remove key/value from dict.
    def change_markbook(self, element):
        if element in self.markbook:
            self.markbook.pop(element)
            print("{} deleted".format(element))
        else:
            print("Element not recognised")

    def display_markbook(self):
        print("Current Markbook entries")
        self.display_date_today()
        for key, value in self.markbook.items():
            print(key, " : ", value)


    def average_mark(self):
        grades = self.markbook.values()
        number_of_grades = len(grades)
        total_grades = int(sum(grades))
        average = int(total_grades / number_of_grades)
        print("Average grade: {} ".format(average))



# CREATE INSTANCES:
# CFG_1 = CFGStudent("Amy", "Fowler", "100373", 1, ["python"])
CFG_2 = CFGStudent("Fleur", "Gill", "200495", 2, ["SQL"])
print(CFG_2.cfg_courses)
print(CFG_2.find_age())
# TRYING METHODS
# print(CFG_1.fullname())
# print(CFGStudent.num_of_students)
# print(Student.display_student(CFG_1))
CFG_2.view_subjects()

CFG_2.add_courses("HTML")
CFG_2.view_subjects()
# CFG_2.view_subjects()
# CFG_2.remove_courses("HTML")
# CFG_2.view_subjects()
CFG_2.add_markbook("code challenge", 45.67)
CFG_2.add_markbook("Theory1", 49.455)

# CFG_2.display_markbook()
# CFG_2.average_mark()

CFG_2.change_markbook("Theory1")
# CFG_2.change_markbook("Theo1")
CFG_2.display_markbook()


# CHECKING INHERITANCE
# print(help(CFGStudent))


