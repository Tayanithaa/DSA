class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=1
        n=len(nums)

        current=1
        for i in range(1,n):
            if  nums[i]<nums[i-1]:
                current+=1
            else:
                current=1
            ans=max(ans,current)
        
        current=1
        for i in range(1,n):
            if  nums[i]>nums[i-1]:
                current+=1
            else:
                current=1
            ans=max(ans,current)
        return ans
