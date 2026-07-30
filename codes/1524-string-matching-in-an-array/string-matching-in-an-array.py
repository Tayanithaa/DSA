class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output=[]
        for i in words:
            for j in words:
                if i!=j and i in j:
                    output.append(i)
                    break
        return output