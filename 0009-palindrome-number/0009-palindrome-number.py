class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        
        if x < 0:
            return False
        else:
            return self.isPalindromeStr(x_str)
        
    def isPalindromeStr(self, x_str: str) -> bool:
        if not x_str:
            return True
        elif x_str[0] == x_str[-1]:
            return self.isPalindromeStr(x_str[1:-1])
        else:
            return False
        