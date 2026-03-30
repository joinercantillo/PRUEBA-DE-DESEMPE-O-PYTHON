def search(studentlist):
    import os
    import csv
    print("\n=== SEARCH STUDENT ===")
    id = input("Enter the Student ID to search: ")
    found_students = [c for c in studentlist if c['Student ID'].lower() == id.lower()]
    
    if found_students:
        print("\nClient(s) found:")
        for student in found_students:
            print(f"  Student ID: {student['Student ID']}, Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}, State: {student['State']}")
    else:
        print(f"No Students found with the ID '{id}'.")
    
    return studentlist