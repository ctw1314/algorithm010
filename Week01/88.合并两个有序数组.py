
# 1. sort排序

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)


# 2. 双指针
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        while j < n:
            if i >= m+j: 
                nums1[i:i+n-j] = nums2[j:n]
                break
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1[i], nums1[i+1:] = nums2[j], nums1[i:len(nums1)-1]
                j += 1; i += 1