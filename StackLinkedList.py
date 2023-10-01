# Stack implementation using Linked List at Begining Insertion and Deletion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None

    def pushElement(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        new_node.next = temp
        self.head = new_node

    def popElement(self):
        temp = self.head
        self.head = temp.next
        temp = None

    def printStack(self):
        temp = self.head
        print(temp.data, end = " ")

        while temp.next:
            temp = temp.next
            print(temp.data, end = " ")

    def peekStack(self):
        temp = self.head
        print(temp.data)

    def reverseStack(self, head):
        if head is None:
            return
        if head.next:
            self.reverseStack(head.next)
        print(head.data,end=" ")

print("0.Exit  1.Push Element  2.Pop Element  3.Display Stack  4.Peek in Stack  5.Reverse Stack")
num = 1
obj = StackLinkedList()

while num!=0:
    num = int(input("Enter the Opearation : "))

    if num==1:
        data = int(input("Enter the element to Push : "))
        obj.pushElement(data)

    elif num==2:
        obj.popElement()

    elif num==3:
        obj.printStack()
        print()

    elif num==4:
        obj.peekStack()

    elif num==5:
        temp = obj.head
        print("Reversed Stack : ", end = " ")
        obj.reverseStack(temp)
        print()
       

    elif num==0:
        print("Thank You! You exited")
        break

    else:
        print("Wrong Input! Try again")

