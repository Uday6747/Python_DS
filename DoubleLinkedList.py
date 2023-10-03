# Implementation of Double Linked List
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insertElement(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def deleteElement(self, data):
        temp = self.head

        if temp is None:
            return
        
        if temp and temp.data == data:
            if temp.next:
                temp.next.prev = None
            self.head = temp.next
            return

        while temp:
            if temp.data == data:
                if temp.next:
                    temp.next.prev = temp.prev
                if temp.prev:
                    temp.prev.next = temp.next
                return
            temp = temp.next


    def displayList(self):
        temp = self.head
        print(temp.data, end = " ")

        while temp.next:
            temp = temp.next
            print(temp.data, end = " ")
        print()

obj = DoubleLinkedList()

num = 1
print("1.Insert Element  2.Delete Element  3.Display List  0.Exit")

while num!=0:
    num = int(input("Enter the Operation : "))
    if num == 1:
        data = int(input("Enter the element to insert : "))
        obj.insertElement(data)
    
    elif num == 2:
        data = int(input("Enter the data to delete : "))
        obj.deleteElement(data)

    elif num == 3:
        obj.displayList()

    elif num == 0:
        print("Thank You")
        break

    else: 
        print("Wrong Choice! Try Again")
