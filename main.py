# main.py

from models import Student

def display_menu():
    print("\n--- CLI Student Grade Manager ---")
    print("1. Add a new student")
    print("2. Assign a grade to a student")
    print("3. View student details & average")
    print("4. View all students")
    print("5. Exit")

def main():
    students_list = []  # List/Array data structure to hold Student objects

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            new_student = Student(student_id, name)
            students_list.append(new_student)
            print(f"Student '{name}' added successfully!")

        elif choice == '2':
            student_id = input("Enter Student ID: ")
            
            # Search for the student
            found_student = None
            for student in students_list:
                if student.student_id == student_id:
                    found_student = student
                    break
            
            if found_student:
                subject = input("Enter Subject Name: ")
                try:
                    grade = float(input(f"Enter Grade for {subject}: "))
                    found_student.add_grade(subject, grade)
                    print(f"Grade added for {found_student.name}.")
                except ValueError:
                    print("Invalid grade. Please enter a number.")
            else:
                print("Student not found.")

        elif choice == '3':
            student_id = input("Enter Student ID: ")
            found_student = None
            for student in students_list:
                if student.student_id == student_id:
                    found_student = student
                    break
            
            if found_student:
                print(f"\n--- {found_student.name} ({found_student.student_id}) ---")
                if found_student.grades:
                    for subject, grade in found_student.grades.items():
                        print(f"{subject}: {grade}")
                    print(f"Average Grade: {found_student.get_average():.2f}")
                else:
                    print("No grades recorded yet.")
            else:
                print("Student not found.")

        elif choice == '4':
            print("\n--- All Enrolled Students ---")
            if not students_list:
                print("No students in the system.")
            for student in students_list:
                print(f"[{student.student_id}] {student.name} - Average: {student.get_average():.2f}")

        elif choice == '5':
            print("Exiting Grade Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()