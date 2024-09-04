import pandas as pd
import random
from faker import Faker

fake = Faker()

# Parameters
NUM_STUDENTS = 50000
NUM_FACULTIES = 1000
NUM_DEPARTMENTS = 30
NUM_COURSES = 500
NUM_CLASSES = 100
NUM_LABS = 50
NUM_BUILDINGS = 10  # Number of blocks (A, B, C, etc.)
NUM_FLOORS = 5  # Floors per block

# Department-specific course names
course_catalog = {
    "Computer Science": [
        "Data Structures and Algorithms",
        "Operating Systems",
        "Computer Networks",
        "Database Management Systems",
        "Machine Learning",
        "Artificial Intelligence",
        "Software Engineering",
        "Cyber Security",
        "Cloud Computing",
        "Distributed Systems"
    ],
    "Mechanical Engineering": [
        "Thermodynamics",
        "Fluid Mechanics",
        "Strength of Materials",
        "Manufacturing Processes",
        "Heat Transfer",
        "Machine Design",
        "Automobile Engineering",
        "Robotics",
        "CAD/CAM",
        "Engineering Mechanics"
    ],
    "Electrical Engineering": [
        "Circuit Theory",
        "Electromagnetic Fields",
        "Control Systems",
        "Power Electronics",
        "Electrical Machines",
        "Power Systems",
        "Digital Electronics",
        "Microprocessors",
        "Signal Processing",
        "Renewable Energy Systems"
    ],
    "Civil Engineering": [
        "Structural Analysis",
        "Construction Materials",
        "Geotechnical Engineering",
        "Surveying",
        "Hydraulics",
        "Transportation Engineering",
        "Environmental Engineering",
        "Concrete Technology",
        "Urban Planning",
        "Steel Structures"
    ],
    "Humanities": [
        "Introduction to Psychology",
        "Sociology of Gender",
        "Philosophy of Ethics",
        "World History",
        "Political Science",
        "Art History",
        "Creative Writing",
        "Cultural Anthropology",
        "Economics for Social Sciences",
        "Mass Communication"
    ],
    # Add more departments as needed
}

# Helper functions
def generate_department_data():
    departments = list(course_catalog.keys())
    department_data = []
    for i, dept_name in enumerate(departments):
        department_data.append({
            'Department_ID': i + 1,
            'Department_Name': dept_name
        })
    return department_data

def generate_course_data(departments):
    courses = []
    for dept in departments:
        dept_name = dept['Department_Name']
        dept_courses = course_catalog.get(dept_name, [])
        for i, course_name in enumerate(dept_courses):
            courses.append({
                'Course_ID': len(courses) + 1,
                'Course_Name': course_name,
                'Department_ID': dept['Department_ID'],
                'Credits': random.choice([2, 3, 4]),
                'Semester': random.choice([1, 2, 3, 4, 5, 6, 7, 8]),
            })
    return courses

def generate_student_data(departments):
    students = []
    for i in range(NUM_STUDENTS):
        dept = random.choice(departments)
        admission_year = random.randint(2019, 2024)
        course_code = dept['Department_Name'][0:4].upper()
        admission_number = f"{admission_year % 100}{course_code}{str(random.randint(1000, 9999)).zfill(4)}"
        enrollment_number = f"{admission_year}{str(random.randint(100000000000, 999999999999))}"

        students.append({
            'Student_ID': i + 1,
            'Name': fake.name(),
            'Age': random.randint(18, 25),
            'Gender': random.choice(['Male', 'Female']),
            'Department_ID': dept['Department_ID'],
            'Year': random.choice([1, 2, 3, 4]),
            'CGPA': round(random.uniform(5.0, 10.0), 2),
            'Email': fake.email(),
            'Admission_Number': admission_number,
            'Enrollment_Number': enrollment_number
        })
    return students

def generate_faculty_data(departments):
    faculties = []
    for i in range(NUM_FACULTIES):
        dept = random.choice(departments)
        faculties.append({
            'Faculty_ID': i + 1,
            'Name': fake.name(),
            'Age': random.randint(30, 60),
            'Gender': random.choice(['Male', 'Female']),
            'Department_ID': dept['Department_ID'],
            'Email': fake.email(),
            'Position': random.choice(['Professor', 'Associate Professor', 'Assistant Professor'])
        })
    return faculties

def generate_class_data():
    classes = []
    for block in range(NUM_BUILDINGS):
        for floor in range(1, NUM_FLOORS + 1):
            for room_number in range(1, NUM_CLASSES // (NUM_BUILDINGS * NUM_FLOORS) + 1):
                block_name = chr(65 + block)  # Converts 0 to 'A', 1 to 'B', etc.
                room_id = f"{block_name}-{floor}{str(room_number).zfill(2)}"
                classes.append({
                    'Class_ID': len(classes) + 1,
                    'Building_Name': f"{block_name} Block",
                    'Room_Number': room_id,
                    'Capacity': random.randint(30, 150)
                })
    return classes

def generate_lab_data():
    labs = []
    for block in range(NUM_BUILDINGS):
        for lab_number in range(1, NUM_LABS // NUM_BUILDINGS + 1):
            block_name = chr(65 + block)
            lab_id = f"{block_name}-Lab{lab_number}"
            labs.append({
                'Lab_ID': len(labs) + 1,
                'Lab_Name': lab_id,
                'Equipment': random.choice(['Computers', 'Chemistry Equipment', 'Mechanical Tools']),
                'Capacity': random.randint(20, 60)
            })
    return labs

def generate_timetable_data(students, faculties, courses, classes):
    timetable = []
    for student in students:
        course = random.choice(courses)
        faculty = random.choice(faculties)
        class_room = random.choice(classes)

        timetable.append({
            'Student_ID': student['Student_ID'],
            'Course_ID': course['Course_ID'],
            'Faculty_ID': faculty['Faculty_ID'],
            'Class_ID': class_room['Class_ID'],
            'Day': random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']),
            'Time': random.choice(['9:00-10:00', '10:00-11:00', '11:00-12:00', '2:00-3:00', '3:00-4:00'])
        })
    return timetable

# Generate data
departments = generate_department_data()
courses = generate_course_data(departments)
students = generate_student_data(departments)
faculties = generate_faculty_data(departments)
classes = generate_class_data()
labs = generate_lab_data()
timetable = generate_timetable_data(students, faculties, courses, classes)

# Convert to DataFrames
df_departments = pd.DataFrame(departments)
df_courses = pd.DataFrame(courses)
df_students = pd.DataFrame(students)
df_faculties = pd.DataFrame(faculties)
df_classes = pd.DataFrame(classes)
df_labs = pd.DataFrame(labs)
df_timetable = pd.DataFrame(timetable)

# Save to JSON files for timetable generation
df_departments.to_json('departments_timetable.json', orient='records', lines=True)
df_courses.to_json('courses_timetable.json', orient='records', lines=True)
df_students.to_json('students_timetable.json', orient='records', lines=True)
df_faculties.to_json('faculties_timetable.json', orient='records', lines=True)
df_classes.to_json('classes_timetable.json', orient='records', lines=True)
df_labs.to_json('labs_timetable.json', orient='records', lines=True)
df_timetable.to_json('timetable.json', orient='records', lines=True)

# Machine Learning Format (Feature Rich)
df_students_ml = df_students[['Student_ID', 'Name', 'Age', 'Gender', 'Department_ID', 'Year', 'CGPA']]
df_faculties_ml = df_faculties[['Faculty_ID', 'Name', 'Age', 'Gender', 'Department_ID', 'Position']]
df_classes_ml = df_classes[['Class_ID', 'Building_Name', 'Room_Number', 'Capacity']]

# Save for machine learning processing
df_students_ml.to_json('students_ml.json', orient='records', lines=True)
df_faculties_ml.to_json('faculties_ml.json', orient='records', lines=True)
df_classes_ml.to_json('classes_ml.json', orient='records', lines=True)

print("Data generation complete with detailed course names and student names in JSON format!")
