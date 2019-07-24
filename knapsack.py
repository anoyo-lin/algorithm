#!/usr/bin/python3
#have list have m length, item is positive number, give you a target number, get combination of numbers to let the sum as near but not higher as possile with the target number.
class dp(nums[], target):
    def __init__(self):
        self.nums = nums[]
        self.target = target
        self.sums = 0
        for i in range(0, self.nums.length() - 1): 
            self.sums += i

    def dp_sol(self):
        if self.sums < self.target:
            return -1
        dp_lst = [[self.target - 1] self.nums.length() - 1]
        for i in range(0, self.nums.length() - 1):
            dp_lst[i][0] = True

        for i in range(0, self.nums.length()-1):
            for j in range(0, self.target-1):
                if ( j <= nums[i-1]):
                    dp_lst[i][j] = dp_lst[i-1][j]
                elif ( j >= nums[i-1]):
                    dp_lst[i][j] = dp_lst[i-1][j] || dp_lst[i-1][j - nums[i]] && True

        for j in range(self.target, 0):
            if dp_lst[self.nums.length()-1][j]:
                return j

        return 0
    def opted_dp_sol(self):
        if self.sums < self.target:
            return -1
        dp_lst = boolean [self.target-1]
        dp[0] = true
        for i in range(0, self.nums.length()-1):
            for j in range(self.target, self.target-nums[i], -1):
                dp[j] = dp[j]||dp[j- nums[i]]


        for k in range(self.target, 0, -1):
            if dp[j]:
                return j

        return 0


                |-------------weight[i]------------|
i-1 : xxxxxxxxxxZxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxO
i   : xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxmax(O, value(i) + Z)



        
    
