# 1. 对9...处理

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
        digits.insert(0, 1)
        return digits


# 2. 转换类型加一

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ""
        for i in digits:
            a += str(i)
        return list(map(int,str(int(a)+1)))