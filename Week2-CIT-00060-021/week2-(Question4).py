def selection_sort(names):
    n = len(names)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if names[j] < names[min_index]:
                min_index = j
        names[i], names[min_index] = names[min_index], names[i]

N = int(input("Enter the total number of names you want to Sort:"))

names = []
for i in range(N):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

selection_sort(names)
print("\nSorted names:")

for name in names:
    print(name)
