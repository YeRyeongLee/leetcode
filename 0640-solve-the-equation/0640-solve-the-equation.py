class Solution:
    def splitEquation(self, equation: str) -> list:
        
        eq_list = []
        curr_num = equation[0]
        
        for i in range(1, len(equation)):
            if equation[i] in ['+', '-']:
                eq_list.append(curr_num)
                curr_num = equation[i]
            else:
                curr_num += equation[i]
        
        eq_list.append(curr_num)
        
        return eq_list
    
    def calculate(self, eq_list: list):
        coef, constant = 0, 0
        
        for term in eq_list:
            if term == 'x' or term == '+x':
                coef += 1
            elif term == '-x':
                coef += -1
            elif 'x' in term:
                coef += int(term[:-1])
            else:
                constant += int(term)
        
        return coef, constant
        
        
    
    def solveEquation(self, equation: str) -> str:
        eq_left, eq_right = equation.split('=')
        
        eq_left_list = self.splitEquation(eq_left)
        eq_right_list = self.splitEquation(eq_right)
        
        left_coef, left_cons = self.calculate(eq_left_list)
        right_coef, right_cons = self.calculate(eq_right_list)
        
        if left_coef == right_coef:
            if left_cons == right_cons:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            ret_val = (right_cons-left_cons) / (left_coef - right_coef)
            return "x=" + str(int(ret_val))
        
        
        