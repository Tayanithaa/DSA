class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero=[]
        list=[]
        for num in nums:
            if num == 0:
                zero.append(num)
            else:
                list.append(num)
                
        combined = list+zero
        nums[:]=combined
        return nums