# ---------------- Student Class ----------------
# importing Person
from .person import Person


class Student(Person):
    # Constructor
    def __init__(self, name, age, address, student_id):
        # Calling Person's __init__
        super().__init__(name, age, address)

        if not isinstance(student_id, str):
            raise TypeError("Student Id must be string")

        self.student_id = student_id
        self.grades = {}  # {"Math": "A"}
        self.courses = []  # list of courses

    def enroll_course(self, course):
        # Enroll in a specified course.
        if course not in self.courses:
            self.courses.append(course)
            print(f"Enrolled in course {course}")
        else:
            print(f"Already enrolled in course {course}")

    def add_grade(self, subject, grade):
        if subject not in self.courses:
            print(f"Student {self.student_id} is not enrolled in {subject}")
            return
        self.grades[subject] = grade
        print(f"Grade {grade} added for {subject}.")

    def display_student_info(self):
        # Print all student details.
        print("Student Information: ")
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        if self.courses:
            course_list = ', '.join(self.courses)  # converting list to string
        else:
            course_list = 'None'
        print(f"Enrolled Courses: {course_list}")
        if self.grades:
            print("Grades: ")
            for course, grade in self.grades.items():
                print(f"  {course}: {grade} ")
        else:
            print("Grades: None")

    def display_person_info(self):
        data = super().display_person_info()
        data.update({
            "student_id": self.student_id,
            "courses": self.courses,
            "grades": self.grades
        })
        return data
