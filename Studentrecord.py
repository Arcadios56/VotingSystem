# List of available courses (unchangeable)
# Create a Dictionary to store all student records
# Get address (zipcode and city)
# Create student dictionary
# Store student record using name as key

all_courses_offered = {
    "Math", "Physics", "Computer Science", "Biology", "Chemistry",
    "Statistics", "English", "Economics", "History", "Philosophy",
    "Sociology", "Political Science", "Geography", "Psychology", "Art",
    "Music", "Engineering", "Law", "Medicine", "Business"
}


student_records = {}

def create_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student age: ")
    address = input("Enter student name: ")
    
    print("Available courses:", ", ".join(AVAILABLE_COURSES))
    courses_input = input("Enter courses e.g, Math,Physics): ")
      
    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")
    
    student = {
        "name": name,
        "age": age,
        "courses": courses,
        "address": {
            "city": city,
            "zip_code": zip_code
        }
    }
    
    student_records[name] = student
    print(f"Student {name} added successfully!")

def student_record(tope):
    if name not in student_record:
        print(f"No student found with name: {name}")
        return
    
    student = student_records[tope]
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Courses:")
    print(f"City: {student['address']['city']}")
    print(f"Zip Code: {student['address']['zip_code']}")

def student_courses(tope):
    if name not in student_records:
        print(f"No student found with name: {name}")
        return
    
    student = student_records[name]
    print(f"Courses for student found with name {name}:) 

def display_student_zip_code(name):
    if name not in student_records:
        print(f"No student found with name: {name}")
        return
    
   