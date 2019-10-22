#!/usr/bin/python3
class binary(array=[], target):
    def __init__(self):
        self.array=array
        self.target=target
        self.lower_bound=0
        self.upper_bound=self.array.length()-1
    def search(self):
        if self.upper_bound>=self.lower_bound:
            middle = array.length()-1//2
            if self.array[middle] = target:
                return target
            if self.array[middle] > target:
                self.upper_bound=middle-1
                return search()
            else:
                self.lower_bound=middle+1
                return search()
        else:
            return -1
    
#interpolation search
#set the middle with specified value 
#middle = low_id + [ (target-low_value)*(high_id - low_id) / (high_value - low_value)
# 200                              300
#[----------------------x-----------]
# 1                                35
# 1 + [(x-200)/(300-200)] * [35-1]
# low + value ratio * high&low_distance


#ternary search
class ternary(sorted_lst, target):
    def __init__(self):
        self.array = sorted_lst
        self.target = target
        self.length = self.array.length()
        self.low = 0
        self.high = self.length - 1
    def search(self, low, high, target):
        mid1 = low + (high - low)/3
        mid2 = high - (high-low)/3

        if array[mid1] == target:
            return mid1
        if array[mid2] == target:
            return mid2

        if target < array[mid1]:
            return search(self, low, mid1, target)
        if target < array[mid2]:
            return search(self, mid1, mid2, target)
        if target > array[mid2] and target <= array[high]:
            return search(self, mid2, high, target)

        return -1
