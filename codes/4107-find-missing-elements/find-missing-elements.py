class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = set(nums)
        missing = []
        for x in range(min(nums), max(nums) + 1):
            if x not in num:
                missing.append(x)

        return missing