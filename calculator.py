def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
result = dictionary["*"](n1=5,n2= 5)
print(result)
