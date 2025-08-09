import json
import os
from smsclass import Student, Course

# ---------------- Data Storage ----------------
students = {}
courses = {}
DATA_FILE = "school_data.json"
# ---------------- Menu Functions ----------------


def add_student():
    try:
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        student_id = input("Enter Student ID: ")
        if student_id in students:
            print(f"Student ID: {student_id} is already exists!")
            return
        students[student_id] = Student(name, age, address, student_id)
        print(f"Student {name} (ID: {student_id}) added successfully")
    except Exception as e:
        print("Error:", e)


def add_course():
    try:
        course_name = input("Enter course name: ")
        course_code = input("Enter course code: ")
        instructor = input("Enter instructor name: ")
        if course_code in courses:
            print(f"Course code {course_code} already exists!")
            return
        courses[course_code] = Course(course_name, course_code, instructor)
        print("Course added successfully.")
    except Exception as e:
        print("Error:", e)


def enroll_student_in_course():
    student_id = input("Enter Student ID: ")
    if student_id not in students:
        print(f"Student-Id {student_id} not found!")
        return
    course_code = input("Enter Course code: ")
    if course_code not in courses:
        print(f"Course-Id {course_code} not found!")
        return
    student_name = students[student_id].name
    subject = courses[course_code].course_name
    students[student_id].enroll_course(subject)
    courses[course_code].add_student(student_name)


def add_grade_for_student():
    student_id = input("Enter Student ID: ")
    if student_id not in students:
        print(f"Student-Id {student_id} not found!")
        return
    course_code = input("Enter Course code: ")
    if course_code not in courses:
        print(f"Course-Id {course_code} not found!")
        return
    subject = courses[course_code].course_name
    grade = input("Enter grade (e.g., A, B+ ): ")
    students[student_id].add_grade(subject, grade)


def display_student_details():
    student_id = input("Enter Student ID: ")
    if student_id not in students:
        print(f"Student-Id {student_id} not found!")
        return
    students[student_id].display_student_info()


def display_course_details():
    course_code = input("Enter Course code: ")
    if course_code not in courses:
        print(f"Course-Id {course_code} not found!")
        return
    courses[course_code].display_course_info()


def save_data():

    data = {}
    # Convert students to dictionary
    student_data = {}
    for st_id, s in students.items():
        student_data[st_id] = s.display_person_info()

    # Convert courses to dictionary
    course_data = {}
    for c_id, c in courses.items():
        course_data[c_id] = c.course_info()

    # Combine into one dictionary
    data["students"] = student_data
    data["courses"] = course_data

    with open(DATA_FILE, "w") as f:
        # indent=4: makes the JSON output pretty-printed
        json.dump(data, f, indent=4)
    print("Data saved successfully.")


def load_data():
    global students, courses
    students = {}
    courses = {}

    if not os.path.isfile(DATA_FILE):
        print("No saved data found.")
        return

    with open(DATA_FILE, "r") as f:
        data = json.load(f)  # data loaded as dictionary

    # dictionary.get(key, default_value)
    students_data = data.get("students", {})

    for sid, s in students_data.items():
        student = Student(s["name"], s["age"], s["address"], s["student_id"])
        students[sid] = student

    for sid, s in students_data.items():
        students[sid].grades = s.get("grades", {})
        students[sid].courses = s.get("courses", [])

    # dictionary.get(key, default_value)
    courses_data = data.get("courses", {})

    for cid, c in courses_data.items():
        course = Course(c["course_name"], c["course_code"], c["instructor"])
        courses[cid] = course

    for cid, c in courses_data.items():
        courses[cid].students = c.get("students", [])

    print("Data loaded successfully.")

# ---------------- Main Menu ----------------


def main():
    while True:
        print("\n===== School Management System =====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data")
        print("8. Load Data")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            enroll_student_in_course()
        elif choice == "4":
            add_grade_for_student()
        elif choice == "5":
            display_student_details()
        elif choice == "6":
            display_course_details()
        elif choice == "7":
            save_data()
        elif choice == "8":
            load_data()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
