class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        qu = [[root,""]]
        while len(qu) > 0:
            pa = qu.pop(0)
            node = pa[0]
            psf = pa[1]
            psf += " "+str(node.val)
            if self.isGood(psf,node.val):
                ans+=1
                
            if(node.left):
                qu.append([node.left,psf])
            if node.right:
                qu.append([node.right,psf])
                
        return ans
    
    def isGood(self,s,X):
        s = s.split(" ")
        i = 0
        while i < len(s) and s[i] == "":
            i+=1
            
        while i < len(s):
            if int(s[i]) <= X:
                i+=1
                continue
            return False
        
        return True