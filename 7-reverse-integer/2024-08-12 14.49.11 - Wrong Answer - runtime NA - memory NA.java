class Solution {
    public int reverse(int x) {
        
    
        
        int reverse = 0;

        while (x != 0) {
            int digit = x % 10;
            x /= 10;

            reverse = reverse * 10 + digit;
        }

        return reverse;
    }
}
    
    

    
