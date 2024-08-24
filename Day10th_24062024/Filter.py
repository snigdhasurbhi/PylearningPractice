# filter in the python, kind of like a for loop but it filters out the values that we don't want
# its a buit in function filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

def filter_list(input_list):
    filtered_list = []
    for item in input_list:
        if isinstance(item, int) and item % 2 == 0:
            filtered_list.append(item)
    return filtered_list