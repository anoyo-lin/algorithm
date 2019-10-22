#!/usr/bin/python3 #pseudo code
class fib_search(sorted_list, target):
    def __init__(self):
        self.n = sorted_list.length()
        self.target = target
        self.array = sorted_list

    def __fib__(self):
        fib_m_2 = 0
        fib_m_1 = 1
        fib_m = fib_m_2 + fib_m_1
        while fib_m < self.n:
            fib_m_2 = fib_m_1
            fib_m_1 = fib_m
            fib_m = fib_m_1 + fib_m_2
        
        fib_m_2 = fib_m_1
        fib_m_1 = fib_m
        fib_m = fib_m_1 + fib_m_2
        
#a fibonacci number can divide into 13 = 8 + 5 offset = minimum(-1 + fib_m_2, self.n - 1) 
#13 8 5 3 2 1 1 0
#     x x x
        while(fib_m > 1):
            offset = - 1
            i = min(offset + fib_m_2, self.n - 1)

            if self.array[i] < self.target:
                fib_m = fib_m_1
                fib_m_1 = fib_m_2
                fib_m_2 = fib_m - fib_m_1

                offset = i

            elif self.array[i] > self.target:
                fib_m = fib_m_2
                fib_m_1 = fib_m_1 - fib_m_2
                fib_m_2 = fib_m - fib_m_1
            else:
                return i

        if fib_m_1 && arr[offset+1] == x:
            return offset+1
        return -1




