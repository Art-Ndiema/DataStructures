def insertion_sort_employee_records(employee_records):
    for i in range(1, len(employee_records)):
        key = employee_records[i]
        j = i - 1
        while j >= 0 and key[2] < employee_records[j][2]:  
            employee_records[j + 1] = employee_records[j]
            j -= 1
        employee_records[j + 1] = key


employee_records = [
    ("SUSAN", 3243, 5000),
    ("FRED",  1256, 3000),
    ("MIKE",  3053, 7000),
    ("TITUS", 4124, 5500),
    ("WITTNEY", 7989, 6500),
]

print("Employee Records Before Sorting:")
for record in employee_records:
    print(f"Name: {record[0]}, Employee ID: {record[1]}, Salary: {record[2]}")

insertion_sort_employee_records(employee_records)

print("\nEmployee Records After Sorting:")
for record in employee_records:
    print(f"Name: {record[0]}, Employee ID: {record[1]}, Salary: {record[2]}")
