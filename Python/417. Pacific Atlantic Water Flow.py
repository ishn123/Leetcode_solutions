class Solution:
    def pacificAtlantic(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = []
        pac = [[False for i in range(n)] for j in range(m)]
        alt = [[False for i in range(n)] for j in range(m)]
        
        for i in range(n):
            self.dfs(mat,0,i,pac,-1)
            self.dfs(mat,m-1,i,alt,-1)
            
        for i in range(m):
            self.dfs(mat,i,0,pac,-1)
            self.dfs(mat,i,n-1,alt,-1)
            
        for i in range(m):
            for j in range(n):
                if pac[i][j]  and alt[i][j]:
                    ans.append([i,j])
                    
        return ans
        
        
        
    def dfs(self,mat,sr,sc,vis,prev):
        if sr < 0 or sc<0 or sr >= len(mat) or sc >= len(mat[0]):
            return 
        
        if prev != -1 and prev > mat[sr][sc]:
            return
        
        if vis[sr][sc]:return
        
        vis[sr][sc] = True
        self.dfs(mat,sr-1,sc,vis,mat[sr][sc])
        self.dfs(mat,sr+1,sc,vis,mat[sr][sc])
        self.dfs(mat,sr,sc-1,vis,mat[sr][sc])
        self.dfs(mat,sr,sc+1,vis,mat[sr][sc])
        
        return