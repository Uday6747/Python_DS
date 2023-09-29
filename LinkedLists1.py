# To create a single list

class Node:
    def __init__(self, data): # Creating a Node
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printll(self):
        temp = self.head

        while temp: # Can be written as while temp.next != None:
            print(temp.data, end = " ")
            temp = temp.next

firstNode = LinkedList()

firstNode.head = Node(90)
secondNode = Node(12)
thirdNode = Node(78)
fourthNode = Node(32)

firstNode.head.next = secondNode
secondNode.next = thirdNode
thirdNode.next = fourthNode

firstNode.printll()

        
