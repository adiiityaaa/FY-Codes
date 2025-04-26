# Basic version of the code: 

def binarySearch(arr, key, low, high):
    if high >= low:
        mid = low + (high - low) 
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binarySearch(arr, key, mid + 1, high)
        else:
            return binarySearch(arr, key, low, mid - 1)
    else:
        return -1
        
arr = []
n = int(input("Enter the number of elements in the array:\n"))
for i in range(n):
    num = int(input(f"Enter element {i+1}:\n"))
    arr.append(num)
search = int(input("Enter the element to search:\n"))
arr.sort()
result = binarySearch(arr, search, 0, len(arr) - 1)

if result != -1:
    print(f"Element is present at position #{result+1}.")
else:
    print("Element is not present in the array.")
