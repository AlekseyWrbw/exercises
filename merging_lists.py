def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    # Create a dummy node to simplify the merging process
    dummy = ListNode()
    current = dummy

    # Traverse both lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # If there are remaining nodes in either list, append them
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # Return the merged list, which starts from the next of the dummy node
    return dummy.next