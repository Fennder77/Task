def concatenate_arrays(*arrays):#concatenate arrays
    result = []
    for arr in arrays:
        result.extend(arr)
    return result

array1 = [1, 2, 3]
array2 = [4, 5]
array3 = [6, 7, 8, 9]

concatenated_array = concatenate_arrays(array1, array2, array3)
print("Concatenated Array:", concatenated_array)  # Output

def reshape_array(input_array, rows, cols):#reshape array
    if rows * cols != len(input_array):
        return None

    reshaped_array = []#reshaped array
    for i in range(0, len(input_array), cols):#cols
        reshaped_array.append(input_array[i:i + cols])
    return reshaped_array

flat_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reshaped_2d_array = reshape_array(flat_array, 3, 3)
print("Reshaped 2D Array:")
for row in reshaped_2d_array:
    print(row)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
