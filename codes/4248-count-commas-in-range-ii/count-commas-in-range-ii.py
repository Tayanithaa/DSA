class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        max=1000
        while n>=max:
            ans += n-max +1
            max *= 1000
        return ans