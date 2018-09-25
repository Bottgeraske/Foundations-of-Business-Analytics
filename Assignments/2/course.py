class Course():
# Class for constructing course-objects

    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []
        self.assignments = []
        # Calls the add_to_course-method of the teacher-class,
        # to make sure the teacher course is connected with the teacher and not just the other way around
        teacher.add_course(title)
    
    def __str__(self):
        return self.title

    def add_student(self, student):
    # Method for adding adding students to a course (by names, not as objects)
        self.students.append(student)

    def assign_grades(self, students, assignment_grades):
    # Method for adding grades to the students in the course. 
    # First argument is a list of student names, second argument is a list of lists.
    # Each list represents the grades of student with the same position in the list of students
    # A list contains 5 1's or 0's, representing a pass(1) or fail(0) for each of the five assignments in the course
        for i in range(len(assignment_grades)):
            assignment = {}
            for student in students:
                if assignment_grades[students.index(student)][i] == 0:
                    assignment[student] = 'Fail'
                elif assignment_grades[students.index(student)][i] == 1:
                    assignment[student] = 'Pass'
            # The output of the function is a list of dictionaries representing the 5 assignments 
            # With a student name as key and the grade as value
            self.assignments.append(assignment)
    
    def get_assignment_grades(self):
    # Method for viewing the grades given to all students in the 5 assignments of the course
        i = 1
        string = 'Course: ' + self.title + '\n'
        for assignment in self.assignments:
            string += 'Assignment ' + str(i) + ':' + str(assignment) + '\n'
            i += 1
        return print(string)