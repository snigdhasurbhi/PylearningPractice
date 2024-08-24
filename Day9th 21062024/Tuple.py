#tuple #decorator
#tuple is a collection which is ordered and unchangeable
#tuples are written with round brackets
#tuples are immutable
#tuples are faster than lists
#tuples can be used as keys in dictionaries
#tuples can be unpacked
def main():
    #create a tuple
    my_tuple = (1,2,3,4,5)
    #print the tuple
    print(my_tuple)
    #access an element in the tuple
    print(my_tuple[2])
    #loop through the tuple
    for x in my_tuple:
        print(x)
    #check if an element is in the tuple
    if 3 in my_tuple:
        print("Yes")
    #length of the tuple

    #real time where we use tuple

    #we use tuples to return multiple values from a function
def func():
 return (1, 2, 3)
if __name__ == "__main__":
    main()
    a, b, c = func()
    print(a, b, c)
    #we can use tuples to swap two values
    x = 5
    y = 10
    x, y = y, x
    print(x, y)
    #we can use tuples to unpack a list
    my_list = [1, 2, 3]
    a, b, c = my_list
    print(a, b, c)
    #we can use tuples to create a single element tuple
    a = (1,)
    print(a)
    #we can use tuples to create a tuple with a single element
    a = (1)
    print(a)
    #we can use tuples to create a tuple without parentheses
    a = 1,
    print(a)
    #we can use tuples to create a tuple with multiple elements
    a = 1, 2, 3
    print(a)
    #we can use tuples to create a tuple with a single element
    a = (1,)
    print(a)
    #we can use tuples to create a tuple with a single element
    a = (1)
    print(a)