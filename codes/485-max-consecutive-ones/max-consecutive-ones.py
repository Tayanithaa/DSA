class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c =0
        mc=0
        for num in nums:
            if num==1:
                c+=1
                mc=max(c,mc)
            else:
                c =0
        return mc