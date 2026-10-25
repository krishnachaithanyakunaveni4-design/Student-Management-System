# Student Management System

A terminal-based student management application built with Python, MySQL, SQL, and Data Structures and Algorithms (DSA).

## Features

- Add and view students
- Search students by name and ID
- Filter students by course
- Count students per course using SQL `GROUP BY`
- Rank students by marks using a custom merge sort algorithm
- Search for students using a custom linear search algorithm
- Validate user input and handle database errors

## Technologies

- Python
- MySQL
- `mysql-connector-python`
- `python-dotenv`
- Git and GitHub

## Setup

1. Install Python and MySQL.
2. Create a MySQL database named `student_management`.
3. Create the `students` table with the columns required by the application, including `student_id`, `name`, `age`, `email`, `course`, and `marks`.
4. Install dependencies:

   `python3 -m pip install mysql-connector-python python-dotenv`

5. Create a `.env` file in the project directory and configure your database credentials.
6. Run the application:

   `python3 main.py`

## DSA Concepts

- Linear search: finds a student by ID.
- Merge sort: ranks students from highest marks to lowest marks.

## Future Improvements

- Add unit tests
- Improve input validation
- Add student update and delete operations
- Create a web interface

