#这题参考了hint2
#主要用一个hash （curwindow）记录当前子字符串，O(1)判断窗口向右扩大时新字符是不
#是已经在curwindow里了。
#
#第一次提交超时了，主要是range 有性能问题，改用xrange

def lengthOfLongestSubstring(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1

    maxlen = 1 

    slen = len(s)
    for i in xrange(0, slen): # Time Limited if use range, see difference between xrange and range for more detail.
        curwindow = {}
        for j in xrange(i, slen):
            next_char = s[j]
            if next_char in curwindow:
                break
            else:
                curwindow[next_char] = True
        
        if len(curwindow) > maxlen:
            maxlen = len(curwindow)

    return maxlen


import cProfile
cProfile.run('lengthOfLongestSubstring(inputs)')

#print("abc", lengthOfLongestSubstring("abc"))
#print("c", lengthOfLongestSubstring("c"))
#print("cc", lengthOfLongestSubstring("cc"))
#print("abcabcbb", lengthOfLongestSubstring("abcabcbb"))
