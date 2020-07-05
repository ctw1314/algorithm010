class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        res = 0
        res_10 = 0
        for i in range(len(bills)):
            if bills[i]==5:
                res +=1
            elif bills[i]==10 and res>0:
                res -=1
                res_10 +=1
            elif bills[i]==20 and res_10*10+res*5>10 and res>0:
                if res_10>0:
                    res_10 -=1
                    res -= 1
                else:
                    res -= 3
            else:
                return False
        return True