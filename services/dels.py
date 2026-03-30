def delc(studentlist):
    import csv
    import os
    print("\n=== DELETE A STUDENT ===")
    id = input("Enter the student ID to delete: ")
    found = False
    for p in studentlist:
        if p['Student ID'].lower() == id.lower():
            studentlist.remove(p)
            print(f"student '{id}' has been deleted.")
            found = True
            break
    
    if not found:
        print(f"Client '{id}' not found in Student list.")
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