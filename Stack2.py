# Implementation of Stack using Lists, Taking Stack elements as user input

stack = []

while ((len(stack))<5):
    n = int(input("Enter stack element : "))
    stack.append(n)

print(f"Stack : {stack}")
print(f"Length of the Stack : {len(stack)}")

print(f"Popped Element : {stack.pop()}")
print(f"After Pop operatio : {stack}")
