class Solution {
    private boolean knapSack(int[] nums,int sum){
        int size = nums.length;
        
        boolean[] dp = new boolean[sum + 1];
        for (int i = 0;i <= sum;i ++){
           dp[i] = i == nums[0];
        }
        /*0-1 knapsack problem, we must initilized the first True, ie must be the dp[sum = nums[0]] = (nums[0] == nums[0])
        the other ones is set to False
	动态规划算法的优化，二维数组=》一维数组 然后逆序
	因为正序会先求dp[n-1][W] 然后 再求 dp[n][W- v(wt(n-1))]
	这与状态表达式 的 max(dp[n-1][W], dp[n-1][W-v(wt(n-1))]) 不符合
       	*/ 
        for (int i = 1;i < size;i++){
            for (int j = sum;j >= nums[i];j--){
                dp[j] = dp[j] || dp[j-nums[i]];
		/*
		 * 因为是boolean， 只讨论有没有的问题， 所以只初始化一个boolean数组， 然后自bottom to top 的 DP  就可以遍历所有的结果。
		 * 我们只需要知道sum/2 是否存在即可
		 */
            }
        }
        return dp[sum];
    }
    
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int item : nums){
            sum += item;
        }
        
        //如果数组元素和不是2的倍数，直接返回false
        if (sum % 2 != 0)
            return false;
        
        return knapSack(nums,sum/2);
    }
}
--------------------- 
作者：chanmufeng 
来源：CSDN 
原文：https://blog.csdn.net/chanmufeng/article/details/82955730 
版权声明：本文为博主原创文章，转载请附上博文链接！
