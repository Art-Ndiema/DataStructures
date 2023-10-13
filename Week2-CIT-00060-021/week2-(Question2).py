def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    input_list = [10, 15, 11, 8, 5]
    print("Original List:", input_list)
    
    insertion_sort_descending(input_list)
    
    print("Here is the sorted list in descending order:", input_list)
