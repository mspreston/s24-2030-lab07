# CPSC 2030 (Lab_07)

Tuesday, March 5th

**Due**: By the end of the lab (Friday, March 8th)

**Instructions**  
For this lab, you will gain additional exposure to working with inheritance and polymorphism in Python. To do this, we will extend your implementation of the Learning Management System (LMS) in Lab06.  

I have provided you with a new version of `Canvas.py`, which relies on you importing `Resource.py` and `Class.py` and creating `Role.py`. I also have provided you with a colorized UML diagram, showing which class is an ABC (blue) and which classes implement the ABC (yellow) in `Role.py`.

You should satisfy the following requirements:
- Implement the `Role` class as an abstract base class in `Role.py` according to the UML diagram
  -  Abstract properties: `name` + `id`
  -  Abstract methods: `view_courses()` + `add_course()`
- Implement the `Student` class in `Role.py` according to the UML diagram
  -  Inherit from `Role`
  -  Properties (Additional): `grade` + `courses`
  -  Methods (Additional): `take_quiz`, which takes a Quiz instance for a particular student and calls the take_quiz() function of the Quiz instance. 
- Implement the `Instructor` class in `Role.py` according to the UML diagram
  -  Inherit from `Role.py`
  -  Properties (Additional): `rank` + `courses`
  -  Methods (Additional): `manage_courses` 
- Implement the classes so that running `Canvas.py` generates similar (basic) output in the terminal.
