def loop_ll(head):
    temp = head

    node_list = set()

    while temp is not None:
        if temp in node_set:
            return True
        node_list.add(temp)

        temp = temp.next
    
    return False

def loop_ll_optimal(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
        
    return False
    