class Solution
 {
    public boolean isPalindrome(String s) 
    {
        String r="";
        boolean a=false;
        for(int i=s.length()-1;i>=0;i--)
        {
          r = r +s.charAt(i);
        }
        if(s.equals(r))
        {
           System.out.println("true");
           a= true;

        }
        else
        {
            System.out.println("false");
            a=false;
        }
        return a;
    }
 }
        
        
        
    
