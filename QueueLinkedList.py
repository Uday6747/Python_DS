# Queue implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def dequeue(self):
        temp = self.head
        self.head = temp.next
        temp = None

    def displayQueue(self):
        temp = self.head
        print(temp.data, end = " ")

        while temp.next:
            temp = temp.next
            print(temp.data, end = " ")

print("0.Exit  1.Enqueue  2.Dequeue  3.Display Queue")
num = 1
obj = QueueLinkedList()

while num!=0:
    num = int(input("Enter the Operation : "))
    if num==1:
        data = int(input("Enter the data to enqueue : "))
        obj.enqueue(data)

    elif num==2:
        obj.dequeue()
    

    elif num==3:
        obj.displayQueue()
        print()

    elif num==0:
        print("Thank you! You exited.")
        break

    else:
        print("Wrong Input! Try again")


