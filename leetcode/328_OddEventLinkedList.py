# -*-coding=utf8-*-
# 按值
def oddEvenListValue(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    podd_head, podd_tail, peven_head, peven_tail = None, None, None, None
    oddfirst = False
    if head.val % 2 == 1:
	oddfirst = True
	
    p = head
    while p:
	if p.val % 2 == 0:
	    if not peven_head:
		peven_head = p
		peven_tail = p
	    else:
		peven_tail.next = p
		peven_tail = p
	else:
	    if not podd_head:
		podd_head = p
		podd_tail = p
	    else:
		podd_tail.next = p
		podd_tail = p
	
	p = p.next
	
    if oddfirst:
	podd_tail.next = peven_head
	if peven_tail:
	    peven_tail.next = None
	
	return podd_head
    else:
	peven_tail.next = podd_head
	if podd_tail:
	    podd_tail.next = None
	
	return peven_head



# 按下标重分配
def oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
	return head
    
    podd_head, podd_tail, peven_head, peven_tail = None, None, None, None
    if head.next == None:
	return head
    
    i = 1
    p = head
    while p:
	if i % 2 == 0:
	    if not peven_head:
		peven_head = p
		peven_tail = p
	    else:
		peven_tail.next = p
		peven_tail = p
	else:
	    if not podd_head:
		podd_head = p
		podd_tail = p
	    else:
		podd_tail.next = p
		podd_tail = p
	
	p = p.next
	i = i + 1
	
    podd_tail.next = peven_head
    if peven_tail:
	peven_tail.next = None
	return podd_head
