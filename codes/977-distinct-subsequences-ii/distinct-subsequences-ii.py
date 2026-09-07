class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        modulo=10**9 + 7
        last=[0]*26
        for char in s:
            index=ord(char)-ord('a')
            last[index]=(sum(last)+1)%modulo
        return sum(last)%modulo