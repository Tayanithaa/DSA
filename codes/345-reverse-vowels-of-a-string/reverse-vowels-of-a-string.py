class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=[]
        for i in range(len(s)):
            if (s[i]=="a" or s[i]=="i" or s[i]=="o" or s[i]=="e" or s[i]=="u" or 
                s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U"):
                vowels.append(s[i])
        reverse = vowels[::-1]

        slist = list(s)
        index = 0
        
        for i in range(len(slist)):
            if (slist[i]=="a" or slist[i]=="i" or slist[i]=="o" or slist[i]=="e" or slist[i]=="u" or slist[i]=="A" or slist[i]=="E" or slist[i]=="I" or slist[i]=="O" or slist[i]=="U"):
                slist[i] = reverse[index]
                index += 1 
        return "".join(slist)