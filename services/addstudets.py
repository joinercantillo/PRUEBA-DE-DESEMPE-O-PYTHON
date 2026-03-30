def add(studentlist):
    import csv
    import os
    validation = int(input("Do you want to add any student? (yes=1/no=0): "))
    while validation == 1:
        try:
            id = input("Student ID: ")
            name = str(input("Name: "))
            age = int(input("Age: "))
            grade = input("Grade (1-12): ")
            if grade not in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
                grade = input("Enter a valid number please: ")
            state = input("State:1=active, 0=inactive: ")

            if state == '1':
                state = "active"
            elif state == '0':
                state = "inactive"
            elif state not in ['1', '0']:   
                print("Invalid input. Defaulting to 'inactive'.")
                state = "inactive"
            
            studentlist.append({'Student ID': id, 'Name': name, 'Age': age, 'Grade': grade, 'State': state})
            
            # Get the correct CSV file path
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            csv_path = os.path.join(base_dir, 'data', 'student.csv')
            
            with open(csv_path, 'w', newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["Student ID", "Name", "Age", "Grade", "State"])
                writer.writeheader()
                writer.writerows(studentlist)
            
            print(f"Student '{name}' added successfully.")
            validation = int(input("Add another Student? (yes=1/no=0): "))
            if validation == 0:
                print("Returning to main menu...")
        except FileNotFoundError as e:
            print(f"Error: CSV file path not found. {e}")
            break
    return studentlist