class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1=[]
        t1=[]
        for i in range(len(s)):
            s1.append(s[i])
        for j in range(len(t)):
            t1.append(t[j])
        t1.sort()
        s1.sort()
        for  i in range(len(s1)):
            if s1[i]!=t1[i]:
                return t1[i]
        return t1[-1]