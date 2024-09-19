global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Function to process a list of numbers and remove every element that is even
def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]
    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)  # Remove the number if it is even
        local_variable -= 1
    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}  # Duplicates in a set are automatically removed

# Process numbers with a set converted to a list
result = process_numbers()
print(result)

# Function to update a dictionary by adding a new key-value pair
def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

modify_dict()  # Corrected function call, should not include '5'

# Function to update the global variable
def update_global():
    global global_variable
    global_variable += 10
    for i in range(5):
        print(i)
    if my_set is not None and 'key4' in my_dict:  # Corrected condition check
        print("Condition met!")
    if 5 not in my_dict:  # Checks if '5' is a key in the dictionary, not a value
        print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
