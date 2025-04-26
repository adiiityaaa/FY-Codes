#Dynamic Version of the code with user employee management

import pandas as pd
from IPython.display import clear_output

names = []
ages = []
salaries = []
ids = []
genders = []

x = int(input("Enter number for Employees:\n"))
for i in range(x):
    namei = input("Enter Employee Name: ")
    names.append(namei)
    idi = input("Enter Employee ID: ")
    ids.append(idi)
    genderi = input("Enter Employee Gender: ")
    genders.append(genderi)    
    agei = int(input("Enter Employee Age: "))
    ages.append(agei)
    salaryi = int(input("Enter Employee Salary: "))
    salaries.append(salaryi)
    
rawdata = {
    "Name": names,
    "ID": ids,
    "Age": ages,
    "Gender": genders,
    "Salary": salaries 
}

data = pd.DataFrame(rawdata)

while True:
    val = int(input("\n\nAvailable Options:\n\n1. Search by Name\n2. Search by ID\n3. Show Maximum Salary\n4. Show Minimum Salary\n5. Show All Employees\n0. Exit\n"))
    if(val == 1):
        clear_output(wait=True)
        sname = input("Enter Employee Name: ")
        snamer = data[data["Name"] == sname] 
        if(snamer.empty):
            print("\nNo matching Employee found!")
        else:
            print("\nEmployee with Matching Name:\n")
            print(snamer)
    elif(val == 2):
        clear_output(wait=True)
        sid = input("Enter Employee ID: ")
        sidr = data[data["ID"] == sid] 
        if(sidr.empty):
            print("\nNo matching Employee found!")
        else:
            print("\nEmployee with Matching Name:\n")
            print(sidr)
    elif(val == 3):
        clear_output(wait=True)
        maxs = data["Salary"].max()
        maxr = data[data["Salary"] == maxs]
        print("\nMaximum Salary Record:\n")
        print(maxr)
    elif(val == 4):
        clear_output(wait=True)
        mins = data["Salary"].min()
        minr = data[data["Salary"] == mins]
        print("\nMinimum Salary Record:\n")
        print(minr)
    elif(val == 5):
        clear_output(wait=True)
        print("\nAll Employee Record:\n")
        print(data)
    elif(val == 0):
        clear_output(wait=True)
        print("Have a Nice Day!")
        break
    else:
        print("Invalid Option!")
        break

# basic version: [from the classroom]
import pandas as pd

employee_data = { "Name": ["Alice", "Bob", "Charlie", "David",
"Eve"], "Age": [25, 30, 35, 28, 40], "Gender": ["Female", "Male",
"Male", "Male", "Female"], "Salary": [50000, 60000, 75000, 52000,
48000] }

df = pd.DataFrame(employee_data)
print("Employee DataFrame:")
print(df)
max_salary = df["Salary"].max()
max_salary_record = df[df["Salary"] ==
max_salary]
print("\nRecord with Maximum Salary:")
print(max_salary_record)
min_salary = df["Salary"].min()
min_salary_record = df[df["Salary"] == min_salary]
print("\nRecord with Minimum Salary:")
print(min_salary_record)
