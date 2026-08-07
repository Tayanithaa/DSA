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

        result = list(set(nums1) & set(nums2))
        return result