# Queue using the collections module

from collections import deque


queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(f"Queue : {queue}")

print(f"Poped Element : {queue.popleft()}")

# In deque, two sides are open, but in queue the first element should be poped first and we use popleft() to pop the element from the left and the pop() to pop the element from the right

print(f"Queue after the pop operation : {queue}")
