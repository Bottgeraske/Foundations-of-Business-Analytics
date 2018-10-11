# pylint: disable=E0401
# This class handles the initiation of objects from the different classes 
# And the calling of methods connected to these to demonstrate the funtionality of the code.

# Importing classes
from course import Course
from programme import Programme
from person import Student, Teacher

# Populating the code with teachers
teacher1 = Teacher('Raghava Rao Mukkamala')
teacher2 = Teacher('Lester Allan Lasrado')
teacher3 = Teacher('John Smith')

# Population the code with courses
course1 = Course('Foundations of Data Science', teacher1)
course2 = Course('Data Mining, Machine Learning and Deep Learning', teacher3)
course3 = Course('Visual Analytics Course', teacher2)
course4 = Course('Text Analytics Course', teacher3)

# Population the code with a programme
programme1 = Programme('Data Science')

# Adding the courses to a programme
programme1.add_course(course1)
programme1.add_course(course2)
programme1.add_course(course3)
programme1.add_course(course4)

# Population the code with students
student1 = Student('Allan', programme1)
student2 = Student('Bob', programme1)
student3 = Student('Lisa', programme1)
student4 = Student('Sally', programme1)
student5 = Student('Joey', programme1)

# Assigning grades to the assignments of each course. 
# Every list represent the grades of a student in the course (based on the order of students in the course). 1 = pass and 0 = fail.
course1.assign_grades(course1.students,[[1,0,0,1,1],[1,1,0,1,0],[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1]])
course2.assign_grades(course2.students,[[0,1,0,0,1],[1,1,1,1,1],[1,1,1,1,1],[1,0,0,0,1],[1,1,0,1,1]])
course3.assign_grades(course3.students,[[0,0,1,0,1],[1,0,1,1,0],[1,1,1,1,1],[1,1,1,1,0],[1,1,0,0,1]])
course4.assign_grades(course4.students,[[1,1,1,0,0],[0,1,1,0,1],[1,0,1,1,1],[1,1,1,1,0],[1,1,0,1,1]])

# Get the diplomas of every student based on the grades asigned above
student1.get_programme_diploma()
student2.get_programme_diploma()
student3.get_programme_diploma()
student4.get_programme_diploma()
student5.get_programme_diploma()