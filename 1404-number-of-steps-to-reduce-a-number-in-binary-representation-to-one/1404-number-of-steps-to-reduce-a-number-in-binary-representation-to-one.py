class Solution:
    def plus_one(self, s: str) -> str:
        s_int = int(s, 2)
        
        return format(s_int+1, 'b')
        
    def numSteps(self, s: str) -> int:
        cnt = 0
        
        while s != '1':
            if s[-1] == '1':
                s = self.plus_one(s)
            else:
                s = s[:-1]
            
            cnt += 1
        
        return cnt