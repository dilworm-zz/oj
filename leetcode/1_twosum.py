def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        nlen = len(nums)
        for i in range(0, nlen-2):
            for j in range(i+1, nlen-1):
                print(i,j,nums[i] + nums[j], target)
                if (nums[i] + nums[j] == target):
                    return [i,j]




print(twoSum([3,2,4],6))
