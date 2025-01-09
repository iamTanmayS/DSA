class Node:
    def __init__(self, data, nextvar=None):
        self.data = data  # Store the data
        self.next = nextvar  # Pointer to the next node (default is None)

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)  # Initialize the list with a head node

    def insert(self, data):
        # Insert a new node at the head of the list
        newnode = Node(data)  # Create a new node
        newnode.next = self.head  # Point the new node to the current head
        self.head = newnode  # Update the head to the new node
        
    def append(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode
    
    def delete(self,data):
        if not self.head:
            return 
        if self.head.data == data:
            self.head = self.head.next
            return
        
        last = self.head
        while last.next:
            if last.next.data == data:
                last.next = last.next.next
                return
            last = last.next     
        
        
    def display(self):
        # Display all nodes in the list
        current = self.head  # Start from the head
        while current:  # Traverse until the end of the list
            print(current.data, end=" --> ")
            current = current.next
        print("None")  # Indicate the end of the list

# Main execution block
if __name__ == "__main__":
    # Step 1: Create a linked list with the initial value
    ll = LinkedList(10)
    ll.append(50)
    # Step 2: Insert new values into the list
    ll.insert(20)
    ll.insert(30)
    ll.insert(40)
    

    # Step 3: Display the linked list
    ll.display()
