def show(studentlist):
    import csv
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'data', 'student.csv')
    try:
        with open(csv_path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            listdat = list(reader)
            if listdat:
                print("\n=== STUDENTS ===")
                for row in listdat:
                    print(f"Student ID: {row['Student ID']}, Name: {row['Name']}, Age: {row['Age']}, Grade: {row['Grade']}, State: {row['State']}")
            else:
                print("The Student list is empty.")
            return listdat
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
        return []