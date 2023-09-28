# Stack using queue module

from queue import LifoQueue

stack = LifoQueue(maxsize=4)
# maxsize is declared and only based on the maxsize the number of elements can be in the stack. Here only 4 elements can be taken into the stack

stack.put(10) # To push the element into the stack
stack.put(20)
stack.put(30)
stack.put(40)

print(f"Stack : {stack}")
print(f"Stack size : {stack.qsize()}")

print(f"Poped Element : {stack.get()}") # To pop the top element from stack
print(f"Stack size after pop operation : {stack.qsize()}")

print(f"If stack is full then prints true else false : {stack.full()}") # It returns a boolean value, true if the stack is full based on the maxsize and numbers of elements pushed and false if the stack is not full

stack.put(50)
print(stack.full())

print(stack.empty()) # It returns a boolean value, true if the stack is empty based on the maxsize and numbers of elements pushed and false if the stack is not empty

