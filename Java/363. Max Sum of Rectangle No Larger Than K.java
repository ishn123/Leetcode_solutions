class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dp = new int[m+1][n+1];
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1];
            }
        }
        int ans = Integer.MIN_VALUE;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                for(int a = i+1;a<=m;a++){
                    for(int b=j+1;b<=n;b++){
                        int s = dp[a][b] - dp[a][j] - dp[i][b] + dp[i][j];
                        if(s<=k){
                            ans = Math.max(ans,s);
                        }
                    }
                }
            }
        }
        return ans;
    }
}