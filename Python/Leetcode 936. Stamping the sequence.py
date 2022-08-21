###BFS APPROACH TLE
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        src = '?'*len(target)
        ds = 10*len(target)
        qu = [[src,0,[]]]
        vis = {}
        ans = []
        while len(qu) > 0:
            pa = qu.pop(0)
            
            if pa[0] in vis:continue
            vis[pa[0]] = True
            
            if pa[0] == target and pa[1] <= ds:
                ans = pa[2]
                break
            
            for i in range(len(target)):
                if i + len(stamp) - 1 >= len(target):
                    break
                    
                tmp = pa[0][0:i] +  stamp + pa[0][i+len(stamp):]
                if tmp not in vis:
                    qu.append([tmp,pa[1]+1,pa[2]+[i]])
                    
                    
        return ans











########################################









class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target = [ch for ch in target]
        qm = 0
        ans = []
        vis = [False for i in range(len(target))]
        while qm != len(target):
            flag = False
            for i in range((len(target)-len(stamp))+1):
                
                if not vis[i] and self.Possible(target,i,stamp):
                    qm = self.replace(target,i,len(stamp),qm)
                    ans.append(i)
                    vis[i] = True
                    flag = True
                    if qm == len(target):
                        break
                        
            if flag == False:
                return []
            
            
        return ans[::-1]
    
    
    def Possible(self,target,x,stamp):
        i = 0
        while i < len(stamp):
            if target[i+x] != stamp[i] and target[i+x] != '?':
                return False
            i+=1
            
        return True
    
    def replace(self,target,x,m,qm):
        i = 0
        while i < m:
            if target[i+x] != '?':
                qm += 1
                target[i+x] = '?'
                
            i+=1
            
        return qm