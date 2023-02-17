class Solution:
    def str2cnt(self, string):
        cnt = [0 for _ in range(26)]
        
        for char in string:
            char_idx = ord(char) - ord('a')
            cnt[char_idx] += 1
        
        return cnt
    
    def minimum_change_of_less_than(self, a_cnt, b_cnt):
        
        moves = []
        
        for i in range(1, 26):
            a_move = sum(a_cnt[i:])
            b_move = sum(b_cnt[:i])
            
            moves.append(a_move + b_move)
        
        return min(moves)
    
    def minimum_change_of_one_letter(self, a_cnt, b_cnt):

        moves = [0 for _ in range(26)]
        
        a_sum = sum(a_cnt)
        b_sum = sum(b_cnt)
        
        for i in range(26):
            a_move = a_sum - a_cnt[i]
            b_move = b_sum - b_cnt[i]
            
            moves[i] = a_move + b_move
        
        return min(moves)
        
    def minCharacters(self, a: str, b: str) -> int:
        a_cnt = self.str2cnt(a)
        b_cnt = self.str2cnt(b)
        
        print(a_cnt)
        print(b_cnt)
        
        # every letter in a is strictly less than every letter in b in the alphabet
        min_change_1 = self.minimum_change_of_less_than(a_cnt, b_cnt)
        
        # every letter in b is strictly less tahn every letter in a in the alphabet
        min_change_2 = self.minimum_change_of_less_than(b_cnt, a_cnt)
        
        # both a and b consist of only one distinct letter
        min_change_3 = self.minimum_change_of_one_letter(a_cnt, b_cnt)
        
        
        return min(min_change_1, min_change_2, min_change_3)