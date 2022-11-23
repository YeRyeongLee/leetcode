from collections import defaultdict

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        pop_dict = defaultdict(lambda: 0)

        for birth, death in logs:
            for year in range(birth, death):
                pop_dict[year] += 1
        
        max_pop = 0
        max_year = 0
        for year in sorted(pop_dict.keys()):
            if pop_dict[year] > max_pop:
                max_pop = pop_dict[year]
                max_year = year
        
        return max_year