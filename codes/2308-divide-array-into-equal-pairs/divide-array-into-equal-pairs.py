class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = len(nums)
        
        nums.sort()
        
        
        count = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                if count % 2 != 0:
                    return False
                count = 1  

        if count % 2 != 0:
            return False
            
        return True