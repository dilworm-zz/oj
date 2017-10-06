# -*- coding=utf-8 -*-
# 1 去掉前缀空字符
# 2 去掉后缀非 "0" ~ "9" 字符
def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    if str==None or str == "":
        return 0

    slen = len(str)
    trimstr = ""

    newstr = ""
    idx = 0
    while idx < slen:
        if str[idx] != " ":
            break
        else:
            idx = idx + 1

    newstr = str[idx:]
    slen = len(newstr)
    if slen == 0:
        return 0

    if newstr[0] != "+" and newstr[0] != "-" and (newstr[0] < "0" or newstr[0] > "9"):
        return 0
    else:
        trimstr=newstr[0]

    for n in xrange(1, slen):
        if newstr[n] < "0" or newstr[n] > "9":
            break
        else:
            trimstr = trimstr + newstr[n]

    #print("trim ", trimstr)
    if len(trimstr) == 1 and (trimstr[0] == "+" or trimstr[0] == "-"):
        return 0

    i = len(trimstr) - 1 
    val = 0
    multi = 1
    while (i > 0):
        val = val + int(newstr[i]) * multi
        multi = multi * 10
        i = i - 1

    if newstr[0] == "+":
        pass
    elif newstr[0] == "-":
        val = val * -1
    else:
        val = val + int(newstr[0]) * multi

    if val > 2147483647:
        return 2147483647
    elif val < -2147483648:
        return -2147483648
    else:
        return val
    

print(myAtoi(" - 011"))
#print(myAtoi("+-123"))
#print(myAtoi("011"))
#print(myAtoi("-112aba"))
#print(myAtoi("123"))
#print(myAtoi("-123"))
