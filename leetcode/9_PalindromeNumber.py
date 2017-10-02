# -*-coding=utf8-*-

def isPalindrome(x):
    if x < 0:
        return False
    
    if x < 10:
        return True
    

    reverted = 0
    src = x
    multi = 0

    # 什么时候超过了一半
    # 1000
    # 21120
    # 12321
    while (src > reverted and src > multi):
        s = src % 10
        src = src / 10
        reverted = reverted * 10 + s
        if multi == 0:
            multi = 1
        else:
            multi = multi * 10

    
    if multi > reverted:
        return False

    #print(src, reverted)
    if src == reverted:
        return True

    reverted = reverted /10
    if src == reverted:
        return True
    else:
        return False


print(isPalindrome(21120))
print(isPalindrome(1000))
print(isPalindrome(10)) # special case
print(isPalindrome(11))
print(isPalindrome(12))
print(isPalindrome(12321))
print(isPalindrome(121))
print(isPalindrome(1231))
