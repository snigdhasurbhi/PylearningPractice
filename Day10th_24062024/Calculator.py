
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
def calculator(n1, n2, func):
    return func(n1, n2)
print(calculator(2, 3, mul))
print(calculator(2, 3, div))
print(calculator(2, 3, add))
print(calculator(2, 3, sub))