# stack using the collections module

from collections import deque

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)

print(f"Stack : {stack}")

# Stack using collections module is same as implementation of Stack using Lists but the time complexity of Stacks using the collections is 0(1)

print(f"Poped Element : {stack.pop()}")
print(f"Stack after poped operation : {stack}")
