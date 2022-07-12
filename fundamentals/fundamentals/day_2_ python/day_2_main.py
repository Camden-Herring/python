

class Student:
    #constructor
    def __init__(self, first_name, last_name, age, instructor, course):
    # attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.instructor = instructor
        self.course = course
    # Method 
    def print_info(self):
        print(f"Name: {self.first_name} {self.last_name}\n Age: {self.age}\n Instructor: {self.instructor}\n Course: {self.course}")

class Course:
    all_courses = []

    @classmethod
    def print_all_courses(cls):
        for course in cls.all_courses:
            print(course)

    def __init__(self, data):
        self.name = data["name"]
        self.instructors = data["instructors"]
        self.program = data["program"]
        Course.all_courses.append(self)
    
    def print_instructor_list(self):
        for instructor in self.instructors:
            print(instructor)

    def update_instructor(self, new_name, index):
        if index < len(self.instructors):
            self.instructors[index] = new_name

    @staticmethod
    def determine_eligibility(age):
        if age >= 18:
            return True
        return False

    def print_info(self):
        print(f"Program: {self.program} \n Name: {self.name}")
        self.print_instructor_list()

python = {
    "name": "Python/Flask",
    "instructors": ["Alfredo", "Spencer", "Tyler"],
    "program": "Full-Stack"
}

mern = {
    "name": "mern",
    "instructors": ["Alfredo", "Spencer", "Tyler"],
    "program": "Full-Stack"
}

java = {
    "name": "Java",
    "instructors": ["Alfredo", "Spencer", "Tyler"],
    "program": "Full-Stack"
}

course_python = Course(python)

course_mern = Course(mern)

course_java = Course(java)

course_python.update_instructor("Ryan", 2)

student_alex = Student("Alex", "Miller", 20, "Nichole", "Web Fundamentals")

print(f"Instructor Name: {student_alex.instructor.upper()}")

student_alex.print_info()

