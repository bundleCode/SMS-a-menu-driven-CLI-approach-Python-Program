# ----------------------- Course Class -------------------------
class Course:
    # constructor
    def __init__(self, course_name, course_code, instructor):

        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []  # list of student ids

    def add_student(self, student_id):
        #  Add a student to the course.
        if student_id not in self.students:
            self.students.append(student_id)
            print(f"Student {student_id} added to course {self.course_code}")
        else:
            print(
                f"Student {student_id} already enrolled in {self.course_code}")

    def display_course_info(self):
        #  Print course details and enrolled students.
        print("Course Information: ")
        print(f"Course Name: {self.course_name}")
        print(f"Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        if self.students:
            # converting list to string
            students_list = ', '.join(self.students)
        else:
            students_list = 'None'
        print(f"Enrolled Students: {students_list}")

    def course_info(self):
        return {
            "course_name": self.course_name,
            "course_code": self.course_code,
            "instructor": self.instructor,
            "students": self.students
        }
