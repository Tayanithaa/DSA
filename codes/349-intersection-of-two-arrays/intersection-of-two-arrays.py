class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # seta=set(nums1)
        # setb=set(nums2)
        # print(seta & setb)
        seta=set(nums1)
        setb=set(nums2)

        result = list(seta & setb)
        return result