# Basic version of the Code:

def bubble_sort(arr):
    x = len(arr)
    for i in range(x):
        for j in range(0, x - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = []
n = int(input("Enter the number of elements in the array:\n"))
for i in range(n):
    num = int(input(f"Enter element {i+1}:\n"))
    arr.append(num)
bubble_sort(arr)
print("Sorted array is:")
print(arr)
