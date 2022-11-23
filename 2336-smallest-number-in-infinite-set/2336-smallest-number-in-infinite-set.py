class SmallestInfiniteSet:

    def __init__(self):
        self.conseq_smallest = 1
        self.sorted_array = []
        

    def popSmallest(self) -> int:
        
        if self.sorted_array:
            ret_val = self.sorted_array[0]
            self.sorted_array = self.sorted_array[1:]
        else:
            ret_val = self.conseq_smallest
            self.conseq_smallest += 1
        
        return ret_val
        

    def addBack(self, num: int) -> None:
        if num == self.conseq_smallest - 1:
            self.conseq_smallest -= 1
        elif num < self.conseq_smallest and num not in self.sorted_array:
            self.sorted_array.append(num)
            self.sorted_array = sorted(self.sorted_array)
            
    
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)