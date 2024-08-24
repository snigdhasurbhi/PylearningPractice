#constructor uses for intialise the value
#contructor of the instance variable
#Constructor
class Person:
    name=None #instance variable
    age=None
    id=None


    def __init__(self, name, age):# init is function which is used for constructor, self is used for point to current object, name and age is parameter, self.name=name is used for assign the value to instance variable, self.age=age is used for assign the value to instance variable.

        self.name=name
        self.age=age
        print("Constructor is called")
        print(f"Name: {self.name}, Age: {self.age}")
        print(self)
        print(id(self))
        print("--------------")
        # self.id=id(self)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    #Methods/Behaviour
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")
        print(self)
        print(id(self))
        print("--------------")
        # self.id=id(self)

p1=Person("John", 30)
p2=Person("Jane", 25)
print(p1)
print(p2)
print(id(p1))
print(id(p2))
print(p1.greet())
print(p2.greet())
p1.greet()
p2.greet()