a = [-2, 45, 0, 11, -9]

def bubbleSort(array):
    
  #Acessing our elements
  for i in range(len(array)):
    # loop for comparing array elements
    for j in range(0, len(array) - i - 1):
      # leess than sign (<)to sort in descending order
      if array[j] < array[j + 1]:

        # swapping elements if elements are not in their intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp



bubbleSort(a)
print("Here is the original list:",a)
print('Sorted Array in Descending Order:')
print(a)