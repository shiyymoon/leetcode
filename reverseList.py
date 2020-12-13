def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    #不懂这个解法为什么不行
    # if (head is None || head.next is None):
    #     return head
    # p = head
    # q = head
    # while(head):
    #     q = p.next
    #     p.next = q.next
    #     q.next = head
    #     head = q
    # return head.next

    if (head is None):
        return head
    if (head.next is None): 
        return head
    pre = ListNode(0)
    while(head):
        q = head.next
        head.next = pre
        pre = head
        head = q
    return pre.next