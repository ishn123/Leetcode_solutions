class Solution {
    String ans = "";
    public String tree2str(TreeNode root) {
        dfs(root);
        return ans.substring(1,ans.length()-1);
    }
    void dfs(TreeNode root){
        if(root==null)
            return;
        ans+="(" + Integer.toString(root.val);
        if(root.left==null && root.right!=null)
            ans += "()";
        dfs(root.left);
        dfs(root.right);
        ans += ")";
        return;
    }
}