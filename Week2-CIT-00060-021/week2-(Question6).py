def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j][1] < a[j+1][1]:
                a[j], a[j+1] = a[j+1], a[j]

students = [
    (9080, [90, 85, 78, 92, 88, 7, 84, 89, 95, 91]),
    (8945, [85, 88, 92, 79, 90, 94, 87, 82, 91, 89]),
    (4517, [50, 65, 7, 92, 88, 76, 84, 49, 35, 51]),
    (5644, [56, 58, 93, 49, 70, 54, 67, 82, 91, 89]),
    (2320, [8, 76, 78, 56, 88, 76, 84, 89, 95, 91]),
    (2312, [85, 88, 92, 79, 87, 94, 87, 82, 91, 89]),
    (1890, [50, 65, 78, 82, 56, 76, 84, 49, 35, 51]),
    (1001, [56, 58, 93, 49, 64, 54, 67, 82, 91, 89]),
    (2349, [50, 65, 78, 72, 34, 76, 84, 49, 35, 51]),
    (9321, [56, 90, 93, 67, 89, 24, 67, 45, 91, 90]),  
]

for i, student in enumerate(students):
    total_marks = sum(student[1])
    students[i] = (student[0], total_marks)

bubble_sort(students)

print("Top 10 Students:")
for i in range(10):
    roll_number, total_marks = students[i]
    print(f"Roll Number: {roll_number}, Total Marks: {total_marks}")
