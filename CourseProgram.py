"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""

from atexit import register
import CourseClass as cc


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]

    student = cc.Register(name, crn)
    course = cc.Course(name, crn, seats, status)

    print("Student Name:", students[0])
    print("Course Name:", course.get_name())
    print("CRN:", course.get_crn())
    print("Seats Left:", course.get_seats() - 1)
    print("\n")

    print("Student Name:", students[1])
    print("Course Name:", course.get_name())
    print("CRN:", course.get_crn())
    print("Seats Left:", course.get_seats() - 2)
    print("\n")

    print("Student Name:", students[2])
    print("Course Name:", course.get_name())
    print("CRN:", course.get_crn())
    print("Seats Left:", course.get_seats() - 3)
    print("\n")

    print("Student Name:", students[3])
    print("Course Name:", course.get_name())
    print("CRN:", course.get_crn())
    print("Seats Left:", course.get_seats() - 4)
    print("\n")

    print("Sorry " + students[4] + ", registration is closed for " + course.get_name())


main()
