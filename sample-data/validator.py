import json

def validate_json(file_name):
    with open(file_name, 'r') as file:
        try:
            data = json.load(file)
            print(f"{file_name} is valid JSON.")
        except json.JSONDecodeError as e:
            print(f"Error in {file_name}: {e}")

# Validate all JSON files
validate_json('departments_timetable.json')
validate_json('courses_timetable.json')
validate_json('students_timetable.json')
validate_json('faculties_timetable.json')
validate_json('classes_timetable.json')
validate_json('labs_timetable.json')
validate_json('timetable.json')
validate_json('students_ml.json')
validate_json('faculties_ml.json')
validate_json('classes_ml.json')
