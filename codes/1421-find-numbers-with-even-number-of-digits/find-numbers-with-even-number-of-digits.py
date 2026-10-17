class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xount=0
        for num in nums:
            if (len(str(num))%2==0):
                xount+=1
        return xount