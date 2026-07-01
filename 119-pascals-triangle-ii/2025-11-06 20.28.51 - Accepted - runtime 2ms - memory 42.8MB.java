class Solution {
    public List<Integer> getRow(int rowIndex) {
        //List<Integer> r=new List<>();
        List<List<Integer>> p=new ArrayList<>();
        for(int i=0;i<=rowIndex;i++){
            List<Integer> r=new ArrayList<>();
            for(int j=0;j<=i;j++){
                if(j==0||j==i) r.add(1);
                else{
                    List<Integer> a=p.get(i-1);
                    r.add(a.get(j)+a.get(j-1));
                }
            }
            p.add(r);
        }
            return p.get(rowIndex);
    }
}