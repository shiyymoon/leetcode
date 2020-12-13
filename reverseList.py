def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    #不懂这个解法为什么不行
    if head is None or head.next is None: 
        return head
    p = head 
    while p.next:
        q = p.next
        p.next = q.next
        q.next = head
        head = q
    return head