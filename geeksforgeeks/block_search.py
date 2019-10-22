#!/usr/bin/python3
#give you a sorted list, define the step sqrt(list_length), and found 1st bracket upper bound is BIGGER than target, and then using the linear search in the block
class block(array=[], target):
    def __init__(self):
        self.array=array
        self.target=target
        self.step=sqrt(self.array.length())
        self.length=self.array.length()

    def search(self):
        previous = 0
        while self.array[previous] < self.target:
            previous = self.step
            self.step+= self.step
            if self.step >= self.length:
                return -1

        while self.array[previous] < self.target:
            previous+=1
            if previous == step or self.length-1:
                return -1

        if self.array[previous] == self.target:
            return target

        return -1



    
