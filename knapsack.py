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

knapsack II

class item(weight, value):
    def __init__(self):
        self.weight = weight
        self.value = value
        
        
item_lst = [ item(w1, v1), item(w2, v2) ... item(wn, vn) ]

class knapsack(item_lst):
    def __init__(self):
        self.item_lst = item_lst
        self.value_sums = 0
        for item.value in item_lst:
            self.value_sums += item.value

    def solution(self, capacity):
        dp = [[capacity + 1] item_lst.length() + 1]
        for x in range(0, capacity + 1):
            dp[x][0] = 0
        dp[0][item_lst[0].weight] = item_lst[0].value

        for i in range(1, item_lst.length()+1):
            for j in range(0, capacity+1):
                if j < item_lst[i-1].weight:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max ( dp[i-1][j], dp[i-1][j-item_lst[i-1].weight] + item_lst[i-1].value)
        //因为j=capacity 没有的话 会 直接 拿 dp[i-1][j] 的 value 就是从自己上面拿，所以最后一个永远会是最优解
        for j in range(capacity, 0, -1):
            if dp[item_lst.lenght()][j]:
                return dp[item_lst.length()][j]

class opted_knapsack(item_lst):
    def __init__(self):
        self.item_lst = item_lst
        self.value_sums = 0
        for item.value in item_lst:
            self.value_sums += item.value

    def solution(self, capacity):
        dp = [capacity + 1]
        dp[0] = 0
        dp[item_lst[0].weight] = item_lst[0].value
        for i in range(1, item_lst.length()):
            for j in range(capacity, capacity-item_lst[i-1].weight, -1):
                dp[j] = max(dp[j], dp[j-item_lst[i-1].weight] + item_lst[i-1].value)

        return dp[capacity]

        
