def reverse(x):
    if x == 0 or x > 0x7fffffff or x < -0xffffffff:
        return 0

    isNegative = x < 0
    num = str(abs(x))

    reversed_str = ""
    val = 0
    multi = 1
    for ch in num:
        val = val + int(ch) * multi
        multi = multi * 10

    if val > 0x7fffffff:
        return 0

    if isNegative:
        val = -val

    return val


print(reverse(1234))
print(reverse(-1234))
