from array import *

pos = -1

def binsrch(a, x):
    low = 0
    high = len(a) - 1
#low reprsents the lowest limit
#high represents the upper limit
    while low <= high:
        mid = (high + low) // 2

        if a[mid] == x:
            globals()['pos'] = mid
            return True
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return False

a = array('i', [5, 18, 28, 30, 43, 55, 73, 80, 86])

# Ask the user for a number to search for
x = int(input("Enter Your Voter ID to search for: "))

if binsrch(a, x):
    print(f"Your Voter's ID has been found at index {pos}.")
else:
    print("Voter's ID not found in the list.")
