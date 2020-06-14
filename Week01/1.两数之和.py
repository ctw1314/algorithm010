
# 1. 字典

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index , num in enumerate(nums):
            another_num = target - num
            if another_num in dict:
                return [dict[another_num], index]
            dict[num] = index
        return None 