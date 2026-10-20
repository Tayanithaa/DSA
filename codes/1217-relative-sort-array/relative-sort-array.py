class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in arr2:
            for x in arr1:
                if x == i:
                    result.append(x)
        rem=[]
        for x in arr1:
            if x not in arr2:
                rem.append(x)


        rem.sort()
        result.extend(rem)
        return result