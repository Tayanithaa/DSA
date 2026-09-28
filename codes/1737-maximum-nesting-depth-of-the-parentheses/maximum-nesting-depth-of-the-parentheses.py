class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        maxi=0
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
                maxi=max(maxi,count)
            elif s[i]==")":
                count-=1

        return maxi