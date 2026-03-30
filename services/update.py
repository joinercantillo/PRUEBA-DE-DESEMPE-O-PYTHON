def updatec(studentlist):
    import csv
    import os
    print("\n=== UPDATE STUDENT ===")
    id = input("Enter the student id to update: ")
    found = False
    
    for student in studentlist:
        if student['Student ID'].lower() == id.lower():
            newid = input("Enter the new student ID (press Enter to keep current): ") 
            new_name = input("Enter the new student name (press Enter to keep current): ")
            new_age = input("Enter the new student age (press Enter to keep current): ")
            new_grade = input("Enter the new student grade (1-12) (press Enter to keep current)")
            if new_grade not in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
                new_grade = input("Enter a valid number please: ")
            new_state = input("Enter the new state (1=active, 0=inactive, press Enter to keep current): ")
            if new_state not in ['1', '0']:   
                print("Invalid input. Defaulting to 'inactive'.")
                new_state = "inactive" 
            elif new_state == 0:
                new_state = "inactive"
            elif new_state == 1:
                new_state = "active"

            try:
                if newid:
                    student['Student ID'] = newid
                if new_name:
                    student['Name'] = new_name
                if new_age:
                    student['Age'] = new_age
                if new_grade:
                    student['Grade'] = new_grade
                if new_state:
                    student['State'] = new_state

                print("\nStudent updated successfully.")
                found = True
            except ValueError:
                print("Error: Cost must be a number, quantity must be an integer.")
                return studentlist
            break
    
    if not found:
        print(f"Student '{id}' not found.")
    else:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, 'data', 'student.csv')
        try:
            with open(csv_path, 'w', newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["Student ID", "Name", "Age", "Grade", "State"])
                writer.writeheader()
                writer.writerows(studentlist)
        except FileNotFoundError as e:
            print(f"Error saving: {e}")
    
    return studentlist