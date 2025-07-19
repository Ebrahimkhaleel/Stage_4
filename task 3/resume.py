import json
import os
import formatter

# Function to load resume from JSON
def load_resume(filename="resume.json"):
    if not os.path.exists(filename):
        print("resume.json not found!")
        return None
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error loading resume.json!")
        return None

# Function to export resume
def export_resume(resume, format_type):
    if not resume:
        return
    if format_type == '1':
        content = formatter.format_txt(resume)
        filename = "resume.txt"
    else:
        content = formatter.format_md(resume)
        filename = "resume.md"
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Resume exported to {filename}")

# Main program
def main():
    resume = load_resume()
    if not resume:
        return
    while True:
        print("\nResume Generator")
        print("1. Export as TXT")
        print("2. Export as MD")
        print("3. Exit")
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            export_resume(resume, '1')
        elif choice == '2':
            export_resume(resume, '2')
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-3.")

if __name__ == "__main__":
    main()