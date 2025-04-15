class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverted = 0
        original = x

        while original:
            reverted = reverted * 10 + original % 10
            original //= 10
        
        return reverted == x