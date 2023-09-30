# To implement insertion operation in Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        new_node = Node(new_data)
        if prev_node is None:
            print("")
            return

        new_node.next = prev_node.next
        prev_node.next = new_node

    def insetAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

    def printLinkedList(self):

        first = self.head 
        print(first.data, end=" ")
        while (first.next):
            first = first.next
            print(first.data, end = " ")
        print()
            

    def checkElement(self, key):
        temp = self.head
        while temp.next:
            if(key == temp.data):
                print("Element Found in the Linked List") 
            temp = temp.next


    def printll(self):
        temp = self.head

        while temp:
            print(temp.data, end = " ")
            temp = temp.next

    def deleteNode(self):

        temp = self.head

        if temp is None:
            return

        self.head = temp.next
        temp = None

print("1.Insert at Beginning \t2.Insert After \t3.Insert at End \t4.Print Linked-List \t5. Check Element \t6.Delete Node")

num = 10

obj = LinkedList()
while(num!=0):
    num = int(input("Enter the Input : "))

    if num==1:
        data = int(input("Enter the data : "))
        obj.insertAtBeginning(data)

    elif num==2:
        prev_data = int(input("Enter the stat of the node after which you want to insert : "))
        new_data = int(input("Enter the new data : "))
        prev_node = obj.head
        while prev_node and prev_node.data != prev_data:
            prev_node = prev_node.next

        obj.insertAfter(prev_node, new_data)

    elif num==3:
        data = int(input("Enter the data : "))
        obj.insetAtEnd(data)

    elif num==4:
        obj.printLinkedList()

    elif num==5:
        data = int(input("Enter the data to check if present in LinkedList : "))
        obj.checkElement(data)

    elif num==6:
        obj.deleteNode()

    else:
        print("Wrong Input! Try again.")

