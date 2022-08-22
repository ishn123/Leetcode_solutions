import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 1:return True
        if n <= 0:return False
        
        y = math.log2(n)
        if y % 2 == 0:
            return True
        return False