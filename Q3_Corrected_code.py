# Decrypted code of the provide encrypted code

# global_variable = 100
# my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}


# def process_numbers():
#     global global_variable
#     local_variable = 5
#     numbers = [1, 2, 3, 4, 5]

#     while local_variable > 0:
#         if local_variable % 2 == 0:
#             numbers.remove(local_variable)
#         local_variable -= 1

#     return numbers


# my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
# result = process_numbers(numbers=my_set)


# def modify_dict():
#     local_variable = 10
#     my_dict["key4"] = local_variable


# modify_dict(5)


# def update_global():
#     global global_variable
#     global_variable += 10


# for i in range(5):
#     print(i)
#     i += 1

# if my_set is not None and my_dict["key4"] == 10:
#     print("Condition met!")

# if 5 not in my_dict:
#     print("5 not found in the dictionare!")

# print(global_variable)
# print(my_dict)
# print(my_set)


global_variable = 100
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}


def process_numbers():
    global global_variable
    local_variable = 5
    numbers = list(my_set)  # used my_set , Convert set to list
    while local_variable > 0:
        if local_variable % 2 == 0:
            if (
                local_variable in numbers
            ):  # This ensures the number is there in the list before removing it
                numbers.remove(local_variable)
        local_variable -= 1

    return numbers


# Remove duplicate values (sets automatically ensure unique elements
my_set = {1, 2, 3, 4, 5}

# numbers is returned from process_numbers function (no need of a parameter)
result = process_numbers()


def modify_dict():
    local_variable = 10
    my_dict["key4"] = local_variable


# Removed the parameter from the modify function
modify_dict()


# Function to update the global variable
def update_global():
    global global_variable
    global_variable += 10


# fixed unnecessary increment of `i` inside the loop
for i in range(5):
    print(i)


if my_set is not None and my_dict.get("key4") == 10:
    print("Condition met!")


if 5 not in my_dict:
    print("5 not found in the dictionary!")


print(global_variable)
print(my_dict)
print(my_set)
