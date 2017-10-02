# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 遍历获取长度len
# 遍历左边left 和 right , left == right 则为回文数字 
def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """

    llen = 0
    p = head
    while p:
        llen = llen + 1
        p = p.next

    if llen == 1:
        return True

    left = 0
    right = 0

    i = 0
    p = head
    multi = 1
    halflen = llen / 2
    while p:
        if i < halflen:
            left = left * 10 + p.val
        else:
            right = p.val * multi + right
            multi = multi * 10

        p = p.next
        i = i + 1

    if llen % 2 != 0:
        right = right / 10

    return left == right

