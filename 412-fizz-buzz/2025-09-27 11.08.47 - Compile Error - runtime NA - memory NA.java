class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> s=new ArraayList<>();
        for(int i=0;i<=n;i++){
            s.add(i);
            if(i%3==0){
                s.set(i,"Fizz");
            }
        }
    }
}