class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        pali=x[::-1]
        if pali==x:
            return True
        return False
