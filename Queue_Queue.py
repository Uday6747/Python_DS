# Queue implementation using Queue class from queue module

from queue import Queue

q = Queue()
q.put(10)
q.put(20)
q.put(30)
print(f"Queue : {q}")

print(f"Poped Element : {q.get()}")
print(f"Queue size : {q.qsize()}")
print(f"True if Queue is full else False : {q.full()}")
print(f"True if Queue is empty else False : {q.empty()}")
