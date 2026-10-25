import mysql.connector
from db_connection import create_connection
from student import Student


def add_student():
    
  name = input("Enter name: ").strip()

  try:
    age = int(input("Enter age: "))
  except ValueError:
    print("Invalid age. Please enter a whole number.")
    return

  if age < 1 or age > 120:
    print("Age must be between 1 and 120.")
    return

  email = input("Enter email: ").strip()
  course = input("Enter course: ").strip()

  if not name or not email or not course:
    print("Name, email, and course cannot be empty.")
    return

  if "@" not in email or "." not in email.split("@")[-1]:
    print("Please enter a valid email address.")
    return


    connection = create_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        sql = """
        INSERT INTO students (name, age, email, course)
        VALUES (%s, %s, %s, %s)
        """
        values = (name, age, email, course)

        cursor.execute(sql, values)
        connection.commit()

        print("Student added successfully!")

     
    except mysql.connector.IntegrityError as error:
        connection.rollback()

        if error.errno == 1062:
            print("That email address is already registered.")
        else:
            print("Database constraint error:", error)

    except mysql.connector.Error as error:
        connection.rollback()
        print("Database error:", error)

    finally:
        cursor.close()
        connection.close()



def view_students():
    connection = create_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            "SELECT student_id, name, age, email, course FROM students"
        )

        rows = cursor.fetchall()

        if not rows:
            print("No students found.")
            return
        for row in rows:
            student = Student(*row)
            print("--------------------")
            student.display()

    except Exception as error:
        print("Error:", error)

    finally:
        cursor.close()
        connection.close()



def search_student_by_name():
    name = input("Enter student name to search: ").strip()

    connection = create_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        sql = """
        SELECT student_id, name, age, email, course
        FROM students
        WHERE name LIKE %s
        """
        cursor.execute(sql, (f"%{name}%",))
        rows = cursor.fetchall()

        if not rows:
            print("No matching students found.")
            return

        for row in rows:
            student = Student(*row)
            print("--------------------")
            student.display()

    except Exception as error:
        print("Error:", error)

    finally:
        cursor.close()
        connection.close()

def filter_students_by_course():
    course = input("Enter course to filter by: ").strip()

    connection = create_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        sql = """
        SELECT student_id, name, age, email, course
        FROM students
        WHERE course = %s
        """
        cursor.execute(sql, (course,))
        rows = cursor.fetchall()

        if not rows:
            print("No students found for this course.")
            return

        for row in rows:
            student = Student(*row)
            print("--------------------")
            student.display()

    except Exception as error:
        print("Error:", error)

    finally:
        cursor.close()
        connection.close()


def count_students_by_course():
    connection = create_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        sql = """
        SELECT course, COUNT(*) AS total_students
        FROM students
        GROUP BY course
        ORDER BY total_students DESC
        """
        cursor.execute(sql)
        rows = cursor.fetchall()

        if not rows:
            print("No students found.")
            return

        print("\n--- Students Per Course ---")

        for course, total in rows:
            print(f"{course}: {total} student(s)")

    except Exception as error:
        print("Error:", error)

    finally:
        cursor.close()
        connection.close()

from dsa_algorithms import linear_search, merge_sort


def search_student_by_id_dsa():
    try:
        target_id = int(input("Enter student ID: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    connection = create_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT student_id, name, age, email, course, marks
            FROM students
        """)
        students = cursor.fetchall()

        # Use our own linear search algorithm
        result = linear_search(students, target_id)

        if result is None:
            print("Student not found.")
        else:
            print("\nStudent found:")
            print("ID:", result[0])
            print("Name:", result[1])
            print("Age:", result[2])
            print("Email:", result[3])
            print("Course:", result[4])
            print("Marks:", result[5])

    except Exception as error:
        print("Error:", error)

    finally:
        cursor.close()
        connection.close()


def rank_students_by_marks():
    connection = create_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT student_id, name, age, email, course, marks
            FROM students
        """)
        students = cursor.fetchall()

        # Use our own merge sort algorithm
        ranked_students = merge_sort(list(students))

        if not ranked_students:
            print("No students found.")
            return

        print("\n--- Student Rankings ---")

        for rank, student in enumerate(ranked_students, start=1):
            print(
                f"{rank}. {student[1]} | "
                f"Marks: {student[5]} | "
                f"ID: {student[0]}"
            )

    except Exception as error:
        print("Error:", error)

    finally:
        cursor.close()
        connection.close()

