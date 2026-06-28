class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=0
        monday=1
        current =1
        for day in range(1,n+1):
            total+=current
            current+=1
            if day % 7==0:
                monday+=1
                current=monday
        return total