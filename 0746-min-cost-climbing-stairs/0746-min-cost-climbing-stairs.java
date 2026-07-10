class Solution {
    int[] dp=new int[1000];
    public int minCostClimbingStairs(int[] cost) {
        Arrays.fill(dp,-1);
        return Math.min(dfs(cost,0),dfs(cost,1));
    }
    int dfs(int[] cost,int i){
        if(i>=cost.length) return 0;
        if(dp[i]!=-1) return dp[i];
        dp[i]=cost[i]+Math.min(dfs(cost,i+1),dfs(cost,i+2));
        return dp[i];
    }
}