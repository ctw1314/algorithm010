
# 1. 暴力移动

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        for i in range(k):
            nums.insert(0,nums.pop())


# 2. 分块合并，使用数组引用 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]



# 3. 分块数组旋转

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == 0:
            return
        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
        return