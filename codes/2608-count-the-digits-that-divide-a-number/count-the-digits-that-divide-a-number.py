class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        output=0
        for nums in str(num):
            val =int(nums)
            if num % val == 0:
                output +=1
        return output