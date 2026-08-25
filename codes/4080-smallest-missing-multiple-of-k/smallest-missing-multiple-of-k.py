class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num=set(nums)
        current = k
        while True:
            if current not in num:
                return current
            current=current+k