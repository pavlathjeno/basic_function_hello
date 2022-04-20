# Task 1 - printing hello
print("hello")

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

# Task 5 - Handle defaults
def def_arg(hello):
      print(hello + " world")

def_arg("hello")

# Task 6 - who greet who
def who_to_who(send_name, receive_name):
    print(f"{send_name} says hello to {receive_name}")
    
who_to_who(receive_name = "Feri", send_name = "Sanyi")