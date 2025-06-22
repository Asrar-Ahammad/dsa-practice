from typing import Optional, Any


class node:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['node'] = None


class linked_list:
    def __init__(self):
        self.head: Optional[node] = None

    def insert_at_beginning(self, data: Any):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data: Any):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next

        last.next = new_node

    def delete_node(self, key: Any):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        if prev:
            prev.next = temp.next

        temp = None
    
    def insert_node(self, index, data):
        new_node = node(data)

        if index> self.size():
            print(f'The provided index is greater that LL length so the index will be {self.size()}')
            index = self.size()

        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        count = 0
        temp = self.head
        while count < index:
            prev = temp 
            temp = temp.next
            count+=1
        
        new_node.next = prev.next
        prev.next = new_node

    def search(self, val):
        temp = self.head

        while temp:
            if temp.data == val:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
    def size(self):
        count = 0
        temp = self.head

        while temp != None:
            temp = temp.next
            count+=1
        return count
    
ll = linked_list()
ll.append(2)
ll.append(3)
ll.append(4)
ll.insert_at_beginning(5)
ll.display()
ll.delete_node(3)
ll.display()
ll.insert_node(0,45)
ll.display()
print(ll.size())
print(ll.search(40))
