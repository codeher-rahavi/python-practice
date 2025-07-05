import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2:
            return False
        s = 1
        a = num
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                s += i
                s += a // i

        if s == a:
            return True
        else:
            return False


print(Solution().checkPerfectNumber(28))