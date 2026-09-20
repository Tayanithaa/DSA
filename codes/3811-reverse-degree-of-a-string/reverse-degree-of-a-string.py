class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0
        for i in range(len(s)):
            char =s[i]

            reverse=26-(ord(char)-ord('a'))
            pos = i+1
            total+=reverse*pos
        return total