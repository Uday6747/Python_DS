# Full implementaion of Stack using Lists
class Stack_Imp:

    def __init__(self):
        self.stack = []

    def insertElement(self, data):
        self.stack.append(data)

    def popElement(self):
        if ((len(self.stack)) > 0):
            print(f"Popped Element from the stack : {self.stack.pop()}")
        else:
            print("Nothing to Pop. Stack is Empty")

    def printStack(self):
        print(f"Stack : {self.stack}")


    def fixedInsertElement(self, data, n):
        if(len(self.stack))<n:
            self.stack.append(data)
        else:
            print("Stack is Full.")

def selection(obj, s, n, q):
    while q!=0:
        
        if q==1:
            if s==1:
                d = int(input("Enter the Element : "))
                obj.fixedInsertElement(d, n)
            elif s==2:
                d = int(input("Enter the Element : "))
                obj.insertElement(d)
        elif q == 2:
            obj.popElement()
        elif q == 3:
            obj.printStack()
        else:
            print("Wrong Option! Enter again")
        q = int(input("Enter an operation to perform: "))

s = int(input("1. Fixed Sized Stack  2. Dynamic Sized Stack\nEnter your Selection: "))
obj = Stack_Imp()

if s==1:
    print("You have choosen Fixed Size Stack.\n")
    n = int(input("Enter the size of the stack : "))
    print("1.Insert Element  2.Pop Element  3.Print Stack  0.Exit")
    q = int(input("Enter an operation to perform : "))
    selection(obj, s, n, q)

elif s==2:
    print("You have choosen Dynamic Sized Stack")
    print("1.Insert Element  2.Pop Element  3.Print Stack  0.Exit")
    q = int(input("Enter an operation to perform : "))
    selection(obj, s, None, q)

else:
    print("Wrong Choice! Enter again")
    





        
