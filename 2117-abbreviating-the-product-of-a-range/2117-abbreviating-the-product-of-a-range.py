class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        product = 1

        for n in range(left, right+1):
            product *= n
        
        p_str = str(product)

        C = 0
        while C < len(p_str):
            if p_str[len(p_str)-1-C] == '0':
                C += 1
            else:
                break
        
        p_str = p_str[:len(p_str)-C]

        if len(p_str) > 10:
            p_str = p_str[:5] + "..." + p_str[-5:]
        
        p_str += 'e' + str(C)
        
        return p_str