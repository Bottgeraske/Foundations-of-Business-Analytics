class Person():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Student(Person):

    def __init__(self, name, programme):
        super().__init__(name)
        self.programme = programme
        self.courses = programme.courses
        self.distinction = 0
        for course in programme.courses:
            course.add_student(name)
    
    def get_grades(self, course):
        i = 1
        string = 'Course: ' + course.title + '\n'
        for assignment in course.assignments:
            string += 'Assignment ' + str(i) + ':' + str(assignment[self.name]) + '\n'
            i += 1
        return print(string)

    def get_programme_diploma(self):
        print('\n-----DIPLOMA-----\nStudent name:', self.name)
        course_failed = 0
        all_assignments_passed = 0
        for course in self.programme.courses:
            assignment_passed = 0
            for i in range(len(course.assignments)):
                if course.assignments[i][self.name] == 'Pass':
                    assignment_passed += 1
            all_assignments_passed += assignment_passed
            if assignment_passed < 3:
                course_failed = 1
        
        if course_failed > 0:
            print('\nProgramme: FAILED (', str(all_assignments_passed), ' of ', str(len(course.assignments)*len(self.programme.courses)), ' assignments passed)', sep='')
        elif all_assignments_passed > 16:
            print('\nProgramme: PASSED with DISTINCTION (', str(all_assignments_passed), ' of ', str(len(course.assignments)*len(self.programme.courses)), ' assignments passed)', sep='')
        else:
            print('\nProgramme: PASSED (', str(all_assignments_passed), ' of ', str(len(course.assignments)*len(self.programme.courses)), ' assignments passed)', sep='')

        print('\nCourses:')
        for course in self.programme.courses:
            assignment_passed = 0
            for i in range(len(course.assignments)):
                if course.assignments[i][self.name] == 'Pass':
                    assignment_passed += 1
            if assignment_passed >= 3:
                print(course, ': PASSED (with ', str(assignment_passed) + ' of ' + str(len(course.assignments)) + ' assignments passed)', sep='')
            else:
                print(course, ': FAILED (with ', str(assignment_passed) + ' of ' + str(len(course.assignments)) + ' assignments passed)', sep='')
            
class Teacher(Person):

    def __init__(self, name):
        super().__init__(name)
        self.courses = []

    def add_to_course(self, course_title):
        self.courses.append(course_title)