# 这题解法参考 http://blog.csdn.net/linhuanmars/article/details/20888595 
#  以每一个字符和字符空隙为中心，分开向两边比较直到不是回文为至
# 字符n个， 空隙有n-1个， 需要遍历的位置有2n - 1, 
# 分另向两边判断是否为回文需要 0(n) ,所以时间总复杂度为 O(2n-1)*O(n) = O(n^2)

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if s == None or len(s) == 1:
        return s

    slen = len(s)

    maxpsub = s[0]
    for i in xrange(1, 2 * slen):
        tmp = i / 2
        left = None
        right = None
        if i % 2 == 0:
            left = tmp - 1
            right = tmp + 1
        else:
            left = tmp
            right = tmp + 1
            
        while (left >= 0 and right < slen and
                s[left] == s[right]):
            left = left - 1
            right = right + 1
            
        new_palin = s[left + 1: right]
        if len(new_palin) > len(maxpsub):
            print("==", new_palin)
            maxpsub = new_palin


    return maxpsub
                
                

print(longestPalindrome("aba"))
s = 'babad'
print(longestPalindrome(s))
s = 'cbbc'
print(longestPalindrome(s))
s = 'cbbd'
print(longestPalindrome(s))

