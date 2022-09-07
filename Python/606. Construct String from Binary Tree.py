class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        self.ans =''
        self.dfs(root)
        return self.ans[1:-1]
        
        
        
    def dfs(self,root):
        if root == None:
            return 
        
        self.ans += '(' + str(root.val)
        if root.left == None and root.right != None:
            self.ans += '()'
            
        self.dfs(root.left)
        self.dfs(root.right)
        self.ans += ')'
        return