class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        z = len(nums) + 1
        for n in range(0,z):
            if n not in nums:
                return n
