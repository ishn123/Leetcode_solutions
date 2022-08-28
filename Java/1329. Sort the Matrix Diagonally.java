class Solution {
    public int[][] diagonalSort(int[][] mat) {
        for(int i=0;i<mat[0].length;i++)
            sort(mat,0,i);
        for(int i=0;i<mat.length;i++)
            sort(mat,i,0);
        return mat;
    }
    public void sort(int[][] mat,int row,int column)
    {
        int r=row;
        int c=column;
        List<Integer> list=new ArrayList<>();
        while(r<mat.length&& c<mat[0].length)
        {
            list.add(mat[r][c]);
            r++;
            c++;
        }
        Collections.sort(list);
        r=row;
        c=column;
        int index=0;
        while(r<mat.length && c<mat[0].length)
        {
            mat[r][c]=list.get(index);
            index++;
            r++;
            c++;
        }
    }
}