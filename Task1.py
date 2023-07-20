# Import the array module
import array

# Create an array of integers(целое число с знаком)
my_array = array.array('i', [1, 2, 3, 4, 5])

# Print the original array
print("Original Array:", my_array)

# Accessing array elements
print("Element at index 2:", my_array[3])#c 0.

# Modifying array elements
my_array[1] = 10
print("Modified Array:", my_array)

# Appending elements to the array
my_array.append(6)
my_array.extend([7, 8, 9])
print("After append elements:", my_array)

# Deleting elements from the array
del my_array[0]
print("After delete element at index 0:", my_array)

# Finding the length of the array
array_length = len(my_array)
print("Length of the array:", array_length)

# Finding the maximum and minimum values
max_value = max(my_array)
min_value = min(my_array)
print("Maximum value in the array:", max_value)
print("Minimum value in the array:", min_value)
