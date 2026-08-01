class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # return nums[len(nums)//2]
        leng=len(nums)
        middle=leng//2
        return nums[middle]