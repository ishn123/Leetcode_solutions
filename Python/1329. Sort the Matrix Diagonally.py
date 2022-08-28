class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        a1 = []
        a2 = []
        i = 0
        
        while i < len(mat[0]):
            a = 0
            b = i
            tmp = []
            while a < len(mat) and b < len(mat[0]):
                tmp.append(mat[a][b])
                a+=1
                b+=1
                
            a1.append(tmp)
            i+=1
            
        i = 1
        while i < len(mat):
            a = i
            b = 0
            tmp = []
            while a < len(mat) and b < len(mat[0]):
                tmp.append(mat[a][b])
                a+=1
                b+=1
            a2.append(tmp)
            i+=1
            
        for i in a1:
            i.sort()
        for i in a2:
            i.sort()
        i = 0
        d = 0
        while i < len(mat[0]):
            a = 0
            b = i
            k = 0
            while a < len(mat) and b < len(mat[0]):
                mat[a][b] = a1[d][k]
                a+=1
                b+=1
                k+=1
            
            i+=1
            d+=1  
        i = 1
        d = 0
        while i < len(mat):
            a = i
            b = 0
            k = 0
            while a < len(mat) and b < len(mat[0]):
                mat[a][b] = a2[d][k]
                a+=1
                b+=1
                k+=1
            
            i+=1
            d+=1
        
        return mat