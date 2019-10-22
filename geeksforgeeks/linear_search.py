#!/usr/bin/python3
class linear(array=[], target):
    def __init__(self):
        self.array=array
        self.target=target

    def search(self):
        for i in self.array:
            if i == self.target:
                return i

        return -1
