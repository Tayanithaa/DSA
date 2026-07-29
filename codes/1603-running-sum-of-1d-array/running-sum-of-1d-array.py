class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num=[]
        sum=0
        for i in nums:
            sum+=i
            num.append(sum)
        return num


        # sum=0
        # num=[]
        # for i in range(0,len(nums)):
        #     for j in range(i):
        #         sum=i+j
        #         num.append(sum)
        #         return num
