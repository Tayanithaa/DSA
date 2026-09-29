class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=str(n)
        maxi=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                dig1=int(s[i])
                dig2=int(s[j])
                prod=dig1*dig2
                if prod>maxi:
                    maxi=prod
        return maxi