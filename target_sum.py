#!/usr/bin/python3
#positive number and you can set positive/negeative for every number to the target number and give the amount of solution method

nums = [ 1, 1, 1, 1, 1]
target = 3
class dfs_brute_solution(nums, target):
    def __init__(self):
        self.nums = nums
        self.target = target

    def solution(self):
        if self.nums == NULL or self.nums.length == 0:
            return 0
        retrun dfs(nums, 0, target)

    def dfs(self, nums, index, target):
        if index == self.nums.length:
            if target == 0:
                return 1
            else:
                return 0
        if f(index, target) != Null:
            return f(index, target)
        //get count
        int count = 0
        count += dfs(nums, index+1, target + nums[index])
        count += dfs(nums, index+1, target - nums[index])
        save ( index , target , count)

        return count

class dp_offset:
    def solution:
        offset = sum
        sum = 2*sum
        dp = [[sum + 1] len + 1]
        dp[0][offset] = 1;
        for i=0; i < len i++:
            for j = nums[i] j<= sum - num[i]; j++:
                dp[i+1][j+nums[i]] += dp[i][j]
                dp[i+1][j-nums[i]] += dp[i][j]

        return dp[len][offset + target]
