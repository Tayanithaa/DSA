class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        f1=["q","w","e","r","t","y","u","i","o","p"]
        f2=["a","s","d","f","g","h","j","k","l"]
        f3=["z","x","c","v","b","n","m"]
        result = []
        for i in range(len(words)):
            word = words[i]
            if all(char.lower() in f1 for char in word):
                result.append(word)
            elif all(char.lower() in f2 for char in word):
                result.append(word)
            elif all(char.lower() in f3 for char in word):
                result.append(word)
                
        return result