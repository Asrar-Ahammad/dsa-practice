def size(self, head):
        count = 0
        temp = self.head

        while temp:
            count+=1
            temp = temp.next
        return count

def middle_of_ll(self, head):
    size = self.size(head)
    if size %2 ==0:
        mid = (size//2)+1
    else:
        mid = size//2

    count = 0
    temp = head
    while count < mid:
        count+=1
        temp = temp.next
    
    return temp

def optimal(self, head):
        fast = head
        slow = head

        while fast:
            fast = fast.next.next
            slow = slow.next

        return slow