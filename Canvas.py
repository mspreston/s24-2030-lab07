from Class import Class
from Resource import Quiz, Assignment
from Role import Student, Instructor

if __name__ == "__main__":
    # create users
    cs_instructor = Instructor("Jon Craton", 1, "Assistant Professor")
    math_instructor = Instructor("Justin Lambright", 2, "Professor")
    cs_student = Student("Rodney Raven", 101, "Freshman")
    print('*' * 15)

    # build the intro CS class
    intro_CS = Class("Fundamentals of Computational Thinking and Problem Solving", "Jon Craton", "01/01/2024", "05/31/2024", 10)

    new_quiz = Quiz("Python 101 Quiz", "John Doe", "01/15/2021", ["What is Python?", "What data type uses square brackets?", "Is Python dynamically typed or statically typed?"], ["A programming language", "A list", "dynamically typed"])
    intro_CS.add_resource(new_quiz)
    print('*' * 15)

    # add the intro CS class to the instructor and student
    cs_instructor.add_course(intro_CS)
    cs_student.add_course(intro_CS)
    take_quiz = input("Do you want to take the quiz? (y/n): ")
    if take_quiz.lower() == "y":
        student_grade = cs_student.take_quiz(new_quiz)
        print(f"You received a {student_grade} on the quiz.")
    print('*' * 15)

    # build out more CS assignments
    new_assignment = Assignment("Lab 06", "Jon Craton", "02/26/2024", "03/08/2024", "Polymorpism in Python", 1024)
    intro_CS.add_resource(new_assignment)

    another_assignment = Assignment("Lab 07", "Jon Craton", "03/04/2024", "03/08/2024", "ABCs in Python", 1024)
    intro_CS.add_resource(another_assignment)
    print('*' * 15)

    # create a math class
    calc_I = Class("Calculus I", "Justin Lambright", "01/01/2024", "05/31/2024", 30)
    new_assignment = Assignment("Homework 01", "Justin Lambright", "01/15/2024", "01/22/2024", "Limits", 1024)
    calc_I.add_resource(new_assignment)
    print('*' * 15)

    # add the math class to the instructor and student
    math_instructor.add_course(calc_I)
    cs_student.add_course(calc_I)
    print('*' * 15)

    # display the courses for the instructor and student
    math_instructor.view_courses()
    cs_student.view_courses()
    print('*' * 15)

    # use methods specific to the derived class (not in the ABC)
    math_instructor.manage_courses()
    print('*' * 15)
