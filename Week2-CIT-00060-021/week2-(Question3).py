def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    input_list = [90,57,14,12,23]
    print("Original list:", input_list)
    
    selection_sort(input_list)
    
    print("Here is the sorted list in ascending order:", input_list)
