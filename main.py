
from student_operations import (
    add_student,
    view_students,
    search_student_by_name,
    filter_students_by_course,
    count_students_by_course,
    search_student_by_id_dsa,
    rank_students_by_marks,
)


def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add student")
        print("2. View students")
        print("3. Search student by name")
        print("4. Filter students by course")
        print("5. Count students per course")
        print("6. Exit")
        print("7. Search student by ID (Linear Search)")
        print("8. Rank students by marks (Merge Sort)")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student_by_name()
        elif choice == "4":
            filter_students_by_course()
        elif choice == "5":
            count_students_by_course()
        elif choice == "6":
            print("Goodbye!")
            break
        elif choice == "7":
            search_student_by_id_dsa()
        elif choice == "8":
            rank_students_by_marks()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

