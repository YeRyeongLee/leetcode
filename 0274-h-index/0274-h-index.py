class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_cits = sorted(citations, reverse=True)
        h_idx = 0
        
        print(sorted_cits)
        
        for i, num_of_cit in enumerate(sorted_cits):
            
            if num_of_cit >= i+1:
                h_idx = i+1
            else:
                break
            
            
        return h_idx