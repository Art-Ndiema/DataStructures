def partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def quick_sort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quick_sort(a, low, pi - 1)
        quick_sort(a, pi + 1, high)

a = [21,11,5,78,49,54,72,88]
print('The list is:', a)
size = len(a)
quick_sort(a, 0, size - 1)
print("Sorted list:")
print(a)
