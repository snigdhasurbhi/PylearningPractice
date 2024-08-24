#Loops means repeat a block of code multiple times
#There are two types of loops in python
#1. for loop
#2. while loop

def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
# Print hello 10 times using for loop
for i in range(10):
    print("Hello")