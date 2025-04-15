class Solution:
    def reverse(self, x: int) -> int:
        import math
        digit = 0
        Negative = False

        if x < 0:
            x = -x
            Negative = True

        num = str(x)

        if Negative:
            num = num[0:]

        result = ""
        for i in num:
            result = i + result

        if Negative:
            result = '-' + result

        result = int(result)
        
        if result >= 2**31-1 or result <= -2**31 : return 0
        else :  return result