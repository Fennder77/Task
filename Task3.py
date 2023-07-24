data = [
    # Student records
    [
        {"name": "Slava", "age": 27, "grade": "A"},
        {"name": "Fedy", "age": 31, "grade": "B"},
        {"name": "Roma", "age": 28, "grade": "A+"},
    ],
    # Employee information
    [
        {"name": "Fedy", "position": "Manager", "salary": 40000},
        {"name": "Roma", "position": "Developer", "salary": 50000},
        {"name": "Slava", "position": "Designer", "salary": 45000},
    ],
]

# Function to get data
def get_data(category, index):
    if category < len(data) and index < len(data[category]):
        return data[category][index]
    else:
        return None

# Function to modify data
def set_data(category, index, new_data):
    if category < len(data) and index < len(data[category]):
        data[category][index].update(new_data)
        return True
    else:
        return False

# Accessing student record at index 1
record = get_data(0, 1)
print("Record:", record)  # {'name': 'Fedy', 'age': 31, 'grade': 'B'}

# Modifying employee information at index 2
updated_data = {"position": "Senior Designer", "salary": 50000}
is_updated = set_data(1, 2, updated_data)
print("Is Updated:", is_updated)  # True

# Accessing updated employee information at index 2
updated_employee = get_data(1, 2)
print("Updated Employee:", updated_employee)  # {'name': 'Slava', 'position': 'Senior Designer', 'salary': 50000}