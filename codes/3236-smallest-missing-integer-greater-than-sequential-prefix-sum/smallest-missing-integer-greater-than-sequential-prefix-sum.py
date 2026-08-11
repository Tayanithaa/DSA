class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # lar=nums[-1]
        # return lar+1
        total=nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total+=nums[i]
            else:
                break

        set1=set(nums)
        while total in set1:
            total+=1
        return total