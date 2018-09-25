class Person():
# Super-class for constructing objects of type person
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Student(Person):
# Sub-class of "person"-class for constructing objects of type student. 

    def __init__(self, name, programme):
        # Takes 2 arguments: a name (string) and a programme (object)
        super().__init__(name)
        self.programme = programme
        self.courses = programme.courses
        self.distinction = 0
        # The student is automatically added to all the courses stored in the "courses"-variable of the programme-object 
        # passed when calling the class
        for course in programme.courses:
            course.add_student(name)
    
    def get_grades(self, course):
    # Method for printing a student's grades in the 5 assignments of a course. 
    # Takes a course-object as the only argument and fetches the grades of the student-object calling the method
    # by looking for the student-name in the "assignment"-dictionary of the course
        i = 1
        string = '\nCourse: ' + course.title + '\n'
        for assignment in course.assignments:
            string += 'Assignment ' + str(i) + ':' + str(assignment[self.name]) + '\n'
            i += 1
        return print(string)

    def get_programme_diploma(self):
    # Method for printing a student diploma based on the grades obtained in the 5 assignments of every course the student is taking
        print('\n-----DIPLOMA-----\nStudent name:', self.name)
        course_failed = 0
        all_assignments_passed = 0

        # First checking the overall number of assignments passed, and wether any course was failed (by failing 2 or more assignments)
        for course in self.programme.courses:
            assignment_passed = 0
            for i in range(len(course.assignments)):
                if course.assignments[i][self.name] == 'Pass':
                    assignment_passed += 1
            all_assignments_passed += assignment_passed
            if assignment_passed < 3:
                course_failed = 1
        
        # If any course is failed, the programme as a whole is failed
        if course_failed > 0:
            print('\nProgramme: FAILED (', str(all_assignments_passed), ' of ', str(len(course.assignments)*len(self.programme.courses)), ' assignments passed)', sep='')
        # If no course is failed, and the student has passed more at least 17 assignments, the programme is passed with distinction
        elif all_assignments_passed > 16:
            print('\nProgramme: PASSED with DISTINCTION (', str(all_assignments_passed), ' of ', str(len(course.assignments)*len(self.programme.courses)), ' assignments passed)', sep='')
        # If none of the above is true, the program is passed normally
        else:
            print('\nProgramme: PASSED (', str(all_assignments_passed), ' of ', str(len(course.assignments)*len(self.programme.courses)), ' assignments passed)', sep='')

        print('\nCourses:')

        # The following loop prints the status of the number of assigments passed in every course taken
        for course in self.programme.courses:
            assignment_passed = 0
            for i in range(len(course.assignments)):
                if course.assignments[i][self.name] == 'Pass':
                    assignment_passed += 1
            # A course is passed if 3 or more assignments are passed and failed of less than 3 are passed
            if assignment_passed >= 3:
                print(course, ': PASSED (with ', str(assignment_passed) + ' of ' + str(len(course.assignments)) + ' assignments passed)', sep='')
            else:
                print(course, ': FAILED (with ', str(assignment_passed) + ' of ' + str(len(course.assignments)) + ' assignments passed)', sep='')
            
class Teacher(Person):
# Sub-class of "person"-class for constructing objects of type student. 


    def __init__(self, name):
    # Takes 1 argument, name
        super().__init__(name)
        self.courses = []

    # Method for adding a course to a teacher. 
    # This method is called directly from the courses-class, as a course-object takes a teacher object as an argument
    def add_course(self, course_title):
        self.courses.append(course_title)