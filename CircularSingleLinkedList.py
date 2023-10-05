# To Implement Circular Linked List
import re


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertElement(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        temp = self.head

        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        self.head = new_node

    def deleteElement(self, data):
        if not self.head:
            return

        if self.head.data == data:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            if self.head == self.head.next:
                self.head = None
            else:
                temp.next = self.head.next
                self.head = self.head.next

        else:
            prev = None
            current = self.head

            while True:
                if current.data == data:
                    if prev:
                        prev.next = current.next
                    else:
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        temp.next = current.next
                        self.head = current.next
                    return
                
                prev = current
                current = current.next
                if current == self.head:
                    break

    def displayList(self):
               
        if not self.head:
            return

        temp = self.head
        while True:
            print(temp.data, end = " ")
            temp = temp.next
            if temp == self.head:
                break
        print()

print("1.Insert at Beginning  2.Insert Element 3.Delete Element  4.Display List  5.Exit ")

num = 1

obj = CircularLinkedList()
while(num!=0):
    num = int(input("Enter the Input : "))

    if num==1:
        data = int(input("Enter the data : "))
        obj.insertAtBeginning(data)

    elif num==2:
        data = int(input("Enter the data : "))
        obj.insertElement(data)

    elif num==3:
        data = int(input("Enter the Element to be deleted : "))
        obj.deleteElement(data)

    elif num==4:
        obj.displayList()

    elif num==5:
        print("Thank You.....")
        break

    else:
        print("Wrong Input! Try again.")

        

