class Node:
    def __init__(self,data,next= None,prev= None):
        self.data = data
        self.next = next
        self.prev = prev
class Dll:
    def __init__(self,data):
        self.newnode = Node(data)
        self.head = self.newnode
        self.tail = self.newnode
       
    def insertion(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode
        
    def display_forward(self):
        current = self.head
        while current:
            print(current.data,current.next, end=" -> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data,current.prev,end=" -> ")
            current = current.prev
        print("None")
        
    
dll = Dll(10)  # Create a list with the initial node containing 10
dll.insertion(20)  # Insert 20 at the head
dll.insertion(30)  # Insert 30 at the head

print("Forward display:")
dll.display_forward()  # Expected: 30 -> 20 -> 10 -> None

print("Backward display:")
dll.display_backward()
            
    
        
        
        
        