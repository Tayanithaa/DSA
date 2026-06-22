class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        value =0
        for i in operations:
            if i == "--X" :
                value -=1
            if i == "X--" :
                value -=1 
            if i == "++X" :
                value +=1
            if i == "X++" :
                value +=1  

        return value
        