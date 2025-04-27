# Basic Version of the code:

import numpy as np
from scipy import stats
arr = []
n = int(input("Enter the number of elements in the array:\n"))
for i in range(n):
    num = int(input(f"Enter element {i+1}:\n"))
    arr.append(num)
arr_np = np.array(arr)
print(f"Mean: {np.mean(arr_np)}")
print(f"Standard Deviation: {np.std(arr_np)}")
print(f"Mode: {stats.mode(arr_np)}")  
print(f"Median: {np.median(arr_np)}")
print(f"Minimum Value: {np.min(arr_np)}")
print(f"Maximum Value: {np.max(arr_np)}")
