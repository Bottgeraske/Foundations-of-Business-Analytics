class Programme():

    def __init__(self, title):
        self.title = title
        self.courses = []

    def __str__(self):
        return self.title

    def add_course(self, course):
        self.courses.append(course)
    
    def course_names(self):
        course_names = []
        for course in self.courses:
            course_names.append(str(course))
        return course_names
