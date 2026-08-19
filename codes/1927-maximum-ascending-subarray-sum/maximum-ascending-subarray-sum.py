class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=current=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                current+=nums[i]
            else:
                maxi=max(maxi,current)
                current=nums[i]
        return max(maxi,current)