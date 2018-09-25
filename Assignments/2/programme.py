class Programme():
# Class for constructing programme-objects

    def __init__(self, title):
        self.title = title
        self.courses = []

    def __str__(self):
        return self.title

    # Method for adding course-objects to the programme "courses"-variable
    def add_course(self, course):
        self.courses.append(course)
    
    # Method for printing the names of the course-objects contained in the "courses"-variable
    def course_names(self):
        course_names = []
        for course in self.courses:
            course_names.append(str(course))
        return print(course_names)
