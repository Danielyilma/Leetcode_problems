class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        leng = len(nums1) + len(nums2)
        middle = math.ceil(leng // 2)
        merge = []
        res = None

        l = 0
        r = 0
        
        while l < len(nums1) or r < len(nums2):
            if r >= len(nums2) or (r < len(nums2) and l < len(nums1) and nums1[l] < nums2[r]):
                merge.append(nums1[l])
                l += 1
            elif l >= len(nums1) or nums1[l] >= nums2[r]:
                merge.append(nums2[r])
                r += 1
            
            if len(merge) - 1 == middle:
                if leng % 2 == 0:
                    res = (merge[-1] + merge[-2]) / 2.0
                else:
                    res = merge[-1]
                break
        
        return res
                    