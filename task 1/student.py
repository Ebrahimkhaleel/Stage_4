import json
import os


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores  
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def calculate_grade(self):
        avg = self.average
        if avg < 50:
            return "Fail"
        elif avg < 80:
            return "Pass"
        else:
            return "Excellent"

# Function to add a student
def add_student(students):
    name = input("Enter student name: ")
    try:
        scores = []
        for i in range(3):
            score = float(input(f"Enter score for subject {i+1}: "))
            if score < 0:
                raise ValueError("Scores cannot be negative!")
            scores.append(score)
        students.append(Student(name, scores))
        print(f"{name} added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

# Function to view all students
def view_students(students):
    if not students:
        print("No students in the system.")
        return
    print("\nAll Students:")
    for student in students:
        print(f"Name: {student.name}, Scores: {student.scores}, Average: {student.average:.2f}, Grade: {student.grade}")

# Function to update a student's scores
def update_student(students):
    name = input("Enter student name to update: ")
    for student in students:
        if student.name.lower() == name.lower():
            try:
                scores = []
                for i in range(3):
                    score = float(input(f"Enter new score for subject {i+1}: "))
                    if score < 0:
                        raise ValueError("Scores cannot be negative!")
                    scores.append(score)
                student.scores = scores
                student.average = student.calculate_average()
                student.grade = student.calculate_grade()
                print(f"{name}'s scores updated!")
                return
            except ValueError as e:
                print(f"Error: {e}")
                return
    print(f"Student {name} not found.")


# Function to save students to JSON
def save_to_json(students, filename="students.json"):
    data = [{"name": s.name, "scores": s.scores} for s in students]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print("Data saved to students.json")

# Function to load students from JSON
def load_from_json(filename="students.json"):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return [Student(d["name"], d["scores"]) for d in data]
    except json.JSONDecodeError:
        print("Error loading JSON file. Starting with empty list.")
        return []


# Main program
def main():
    students = load_from_json()
    while True:
        print("\nStudent Report Card App")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Save and Exit")
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            save_to_json(students)
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-4.")

if __name__ == "__main__":
    main()


