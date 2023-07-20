import array

def generate_sequence_array(start, end, step=1):
    return array.array('d', [current_value for current_value in range(start, end+1, step)])

def array_statistics(input_array):
    array_sum = sum(input_array)
    array_average = array_sum / len(input_array)
    array_max = max(input_array)
    array_min = min(input_array)
    return array_sum, array_average, array_max, array_min

def get_user_input():
    input_array = array.array('d')
    print("Enter numeric values to add to the array (enter 'q' to stop):")
    while True:
        user_input = input(">> ")
        if user_input == 'q':
            break
        try:
            value = float(user_input)
            input_array.append(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'q' to stop.")
    return input_array

# Generate array with a sequence of numbers from 1 to 10 with a step of 1
sequence_array = generate_sequence_array(1, 10, 1)
print("Sequence Array:", sequence_array)

# Find the statistics of the sequence array
sum_value, average_value, max_value, min_value = array_statistics(sequence_array)
print("Sum:", sum_value)
print("Average:", average_value)
print("Maximum:", max_value)
print("Minimum:", min_value)

# user to input values into an array
user_array = get_user_input()
print("User Array:", user_array)

# Find the statistics of the array
sum_value, average_value, max_value, min_value = array_statistics(user_array)
print("Sum:", sum_value)
print("Average:", average_value)
print("Maximum:", max_value)
print("Minimum:", min_value)
