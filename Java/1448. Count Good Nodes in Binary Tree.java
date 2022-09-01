class Pair{
    TreeNode node;
    String psf;
    Pair(TreeNode n,String p){
        node  = n;
        psf = p;
    }
}
class Solution {
    public int goodNodes(TreeNode root) {
        Queue<Pair> qu = new ArrayDeque<>();
        qu.add(new Pair(root,""));
        int ans = 0;
        while(qu.size()>  0){
            Pair p = qu.remove();
            TreeNode node = p.node;
            String psf = p.psf;
            psf += " "+Integer.toString(node.val);
            if(isGood(psf,node.val))
                ans++;
            if(node.left!=null)
                qu.add(new Pair(node.left,psf));
            if(node.right!=null)
                qu.add(new Pair(node.right,psf));
        }
        return ans;
    }
    private boolean isGood(String s,int X){
        String[] a = s.split(" ");
        int i=1;
        while(i<a.length){
            if(Integer.parseInt(a[i])<=X){
                i++;
                continue;
            }
            return false;
        }
        return true;
    }
}
