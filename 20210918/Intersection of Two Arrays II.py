import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        col = collections.Counter(nums2)
        for i in nums1:
            if col.get(i):
                if col[i] != 0:
                    res.append(i)
                    col[i] -= 1
        return res