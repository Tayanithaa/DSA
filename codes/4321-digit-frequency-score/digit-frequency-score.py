class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum =0
        while n>0:
            sum +=n%10
            n//=10
        return sum