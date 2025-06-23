class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next= None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_begining(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        count = 0
        temp = self.head

        if index > self.length():
            new_node.prev = self.tail
            self.tail.next = new_node
            return

        while temp is not None and count < index-1:
            temp = temp.next
            count+=1
        
        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node

    def traversal_start(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        
        print("None")
        
    def traversal_end(self):
        temp = self.tail

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("None")

    def peek(self):
        print("Head : ",self.head.data)
        print("Tail : ",self.tail.data)

    def length(self):
        count = 0
        temp = self.head


        while temp:
            temp = temp.next
            count+=1

        return count
    
    def deletion_at_start(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("List is empty.")
    
    def deletion_at_end(self):
        if self.tail is not None:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            print("List is empty.")
        
    def deletion_at_index(self, index):
        if self.head is None:
            print("List is empty.")
            return

        if index < 0 or index >= self.length():
            print("Index out of bounds.")
            return

        if index == 0:
            self.deletion_at_start()
            return

        if index == self.length() - 1:
            self.deletion_at_end()
            return
        count = 0
        temp = self.head
        while temp is not None and count < index:
            temp = temp.next
            count+=1
        
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    

arr = [1,2,3,4,5,6,7,8,9]
dll = DLL()
for i in arr:
    dll.insert_at_end(i)

dll.peek()
dll.insert_at_index(0, 44)

dll.traversal_start()
dll.deletion_at_start()
dll.traversal_start()
dll.deletion_at_end()
dll.traversal_start()
# dll.traversal_end()
dll.deletion_at_index(2)
dll.traversal_start()
