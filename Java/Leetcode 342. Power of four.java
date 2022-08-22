class Solution {
    public boolean isPowerOfFour(int n) {
        if(n==1)return true;
        if(n<=0)return false;
        double y = Math.log(n) / Math.log(2);
        if(y%2==0)
            return true;
        return false;
    }
}