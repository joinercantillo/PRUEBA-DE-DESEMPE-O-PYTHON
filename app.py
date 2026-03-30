import csv
import os
from services.addstudets import add
from services.show import show
from services.dels import delc
from services.seacrh import search
from services.update import updatec

studentlist = []
menu = ["1 - Add Student", 
        "2 - list Student",
        "3 - Delete Student", 
        "4 - Search Student",
        "5 - Update Student Data", 
        "6 - EXIT"]

option = 0

while option != 6: 
    print("\n--- WELCOME TO SCHOOL ***** ---")
    for item in menu:
        print(item)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'data', 'student.csv')
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        alls = list(reader)
    
    
    option = int(input("Select an option (1-7): "))
    
    if option == 1:
        add(alls)
    elif option == 2:
        show(alls)
    elif option == 3:
        delc(alls)
    elif option == 4:
        search(alls)
    elif option == 5:
        updatec(alls)
    elif option == 6:
        print("\nGOODBYE!")
        break
    else:
        print("Invalid option. Please select between 1-7.")