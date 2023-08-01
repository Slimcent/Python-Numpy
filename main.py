import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

#  From the second element, slice elements from index 1 to index 4 (not included)
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

print()

#  From both elements, return index 2
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

print()

#  From both elements, slice index 1 to index 4 (not included), this will return a 2-D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])

print()

#  Change data type from float to integer by using 'i' as parameter value
arr = np.array([1.1, 2.1, 3.1])
new_arr = arr.astype('i')
print(new_arr)
print(new_arr.dtype)

print()

#  Make a copy, change the original array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

print()

# Make a view, change the original array, and display both arrays,
# The view SHOULD be affected by the changes made to the original array
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

print()

#  Print the value of the base attribute to check if an array owns its data or not
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)

print()

#  Shape of an array
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

print()

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

print()

#  Reshape an array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = arr.reshape(4, 3)
print(new_arr)

print()

#  Iterating an array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

#  Iterating arrays using nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)

#  Enumerated iteration using ndenumerate()
for idx, x in np.ndenumerate(arr):
    print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

print()

#  Joining numPy arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

#  Splitting numPy arrays
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 3)
print(new_arr)

arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 4)
print(new_arr)

arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 3)
print(new_arr[0])
print(new_arr[1])
print(new_arr[2])

print()

#  Searching arrays
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 0)  # Find the indexes where the values are even
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 1)  # Find the indexes where the values are odd
print(x)

#  Search sorted, returns the value of the index specified
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')  # starts search from the right
print(x)

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

print()

#  Sorting Arrays
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

#  Filtering Arrays
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is higher than 42, set the value to True, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is completely divisble by 2, set the value to True, otherwise False
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newArray = arr[filter_arr]
print(filter_arr)
print(newArray)

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newArr = arr[filter_arr]
print(filter_arr)
print(newArr)

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newArr = arr[filter_arr]
print(filter_arr)
print(newArr)

