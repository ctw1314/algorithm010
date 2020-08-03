class Solution(object):
    def bitCountA(n):
        count = 0
        while (n != 0):
            if (n & 1 != 0):
                count += 1
            n = n>>1
        return count


    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while (n != 0):
            n = n & (n - 1)
            count += 1
        return count