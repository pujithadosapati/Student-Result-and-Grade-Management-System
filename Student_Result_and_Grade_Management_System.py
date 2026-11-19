# Student Result & Grade Management System
students = {}
# Calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"
# Get valid marks
def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks in {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


# Add student
def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")

    subjects = {}
    n = int(input("Enter number of subjects: "))

    if n <= 0:
        print("Number of subjects must be positive.")
        return

    for i in range(n):
        subject = input(f"Enter subject {i + 1} name: ")
        subjects[subject] = get_marks(subject)

    students[roll] = {
        "name": name,
        "subjects": subjects
    }

    print("Student added successfully!")


# Display student result
def display_student(roll):
    student = students[roll]
    subjects = student["subjects"]

    total = sum(subjects.values())
    maximum = len(subjects) * 100
    percentage = (total / maximum) * 100
    grade = calculate_grade(percentage)

    print("\n----- STUDENT RESULT -----")
    print("Roll Number:", roll)
    print("Name:", student["name"])

    for subject, marks in subjects.items():
        print(subject, ":", marks)

    print("Total Marks:", total, "/", maximum)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)


# View all students
def view_students():
    if not students:
        print("No student records found.")
        return

    for roll in students:
        display_student(roll)


# Search student
def search_student():
    roll = input("Enter Roll Number to search: ")

    if roll in students:
        display_student(roll)
    else:
        print("Student not found!")


# Update student
def update_student():
    roll = input("Enter Roll Number to update: ")

    if roll not in students:
        print("Student not found!")
        return

    print("1. Update Name")
    print("2. Update Marks")

    choice = input("Enter your choice: ")

    if choice == "1":
        students[roll]["name"] = input("Enter new name: ")
        print("Name updated successfully!")

    elif choice == "2":
        subjects = students[roll]["subjects"]

        for subject in subjects:
            subjects[subject] = get_marks(subject)

        print("Marks updated successfully!")

    else:
        print("Invalid choice!")


# Performance summary
def performance_summary():
    if not students:
        print("No student records available.")
        return

    percentages = []

    for roll, student in students.items():
        subjects = student["subjects"]
        total = sum(subjects.values())
        maximum = len(subjects) * 100
        percentage = (total / maximum) * 100
        percentages.append((student["name"], percentage))

    average = sum(p[1] for p in percentages) / len(percentages)

    highest = max(percentages, key=lambda x: x[1])

    print("\n----- PERFORMANCE SUMMARY -----")
    print("Total Students:", len(students))
    print("Class Average:", round(average, 2), "%")
    print("Top Performer:", highest[0])
    print("Highest Percentage:", round(highest[1], 2), "%")


# Main menu
while True:
    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. View All Students")
    print("5. Performance Summary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        view_students()

    elif choice == "5":
        performance_summary()

    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")
