# Task 1 - printing hello
def hello():
    return print("hello")

hello()

# Task 2 - customized print
name = input("Name:")
print(f"hello {name}")

# Task 3 - carry out to function
def inputname():
    name = input("Name:")
    return print(f"hello {name}")

inputname()

# Task 4 - Open to extend

def helloname(name):
    return print(f"hello {name}")


helloname(input("Name:"))