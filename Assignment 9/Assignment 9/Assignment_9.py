# assignment 9 yay

# database of courses and students
courses = {
    "Python": {"Alice", "Bob", "Charlie", "David"},
    "Database": {"Bob", "Eve", "Frank", "Alice"},
    "Networking": {"Charlie", "George", "Alice"},
    "Cybersecurity": {"David", "Eve", "Henry", "Charlie"}
}

# display
print("Course Enrollments")

# lpp to make sure we display everything
for course, students in courses.items():
    print(f"{course}: {students}")



# looking for students that are present in both courses
python_database = courses["Python"] & courses["Database"]
python_cybersecurity = courses["Python"] & courses["Cybersecurity"]

print("")
print("Students in Python and Database:")
print(python_database)

print("")
print("Students in Python and Cybersecurity:")
print(python_cybersecurity)



# all students
all_students = (
    courses["Python"]
    | courses["Database"]
    | courses["Networking"]
    | courses["Cybersecurity"]
)

print("")
print("List of Students:")
print(all_students)

print("")
print("Total unique students:", len(all_students))



# empty set
only_one_course = set()

# counting students
for student_name in all_students:
    course_count = 0

    # count per student
    for students in courses.values():
        if student_name in students:
            course_count += 1

    # adding students only in one course
    if course_count == 1:
        only_one_course.add(student_name)

print("")
print("Students only in one Course:")
print(only_one_course)



# name search
print("")
search_name = input("\nEnter student name: ")
print("")

# Track which courses the student is enrolled in
enrolled_courses = []

# loop to check
for course, students in courses.items():
    if search_name in students:
        enrolled_courses.append(course)

# display
if enrolled_courses:
    print(f"{search_name} is enrolled in:")
    
    for course in enrolled_courses:
        print(course)
else:
    print("Student not found.")