# -*-coding=utf8-*-
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """

    maxarea = 0
    i = 0
    j = len(height) - 1
    while (i < j):
        a = min(height[i], height[j]) * (j - i)
        if a > maxarea:
            maxarea = a

        if height[i] < height[j]:
            i = i + 1
        else:
            j = j - 1

    return maxarea


#print(maxArea([1,1]))
#height = [1,3,6,32,3,6]	
#print(maxArea(height))
#height = [1,3,6,32,3,6,2,1,45,3,53]
#print(maxArea(height))
height = [2,3,4,5,18,17,6]
print(maxArea(height))


