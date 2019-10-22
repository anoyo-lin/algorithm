#!/usr/bin/python3
import binary_search
class doubling_search(sorted_list, target):
    def __init__(self):
        self.array = sorted_list
        self.target = target
        self.low_id = 0
        self.high_id = self.array.length() - 1
        self.length = self.array.length()

    def search(self):
        if self.array[0] == self.target:
            return self.target
        index = 1 
        while index < self.length and  self.array[index] <= self.target:
            index = index * 2
        
        return binary_search(sorted_list, index/2, min(index, self.length, self.target)
#this algorithm is named by exponential search, but it use mutiplication (*2 doubling) instead the exponential calculation.
