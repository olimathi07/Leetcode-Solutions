class Solution {
    public String simplifyPath(String path) {
        String[] p=path.split("/");
        Stack<String> s=new Stack<>();
        for(String w:p){
            if(w.equals("")||w.equals(".")){continue;}
            else if(w.equals("..")) {if(!s.isEmpty()) s.pop();}
            else{s.push(w);}
        }
        return '/'+String.join("/",s);
    }
}