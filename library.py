import psycopg

# Create a Student class
class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def register(self):

        # Connect to PostgreSQL
        with psycopg.connect(
            dbname="library_db",
            user="postgres",
            password="Kevin@46456965",
            host="localhost",
            port="5432"
        ) as conn:

            # Execute SQL command
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO students (name, course) " \
                    "VALUES (%s, %s)",
                    (self.name, self.course)
                )

        print("Student registered successfully!")


# Collect student information
name = input("Enter student name: ")
course = input("Enter student course: ")

# Create a Student object
student1 = Student(name, course)

# Register the student
student1.register()