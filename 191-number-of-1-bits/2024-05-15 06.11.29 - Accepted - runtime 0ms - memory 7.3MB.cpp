class Solution {
public:
    int hammingWeight(int n) {
    int count = (n == 0) ? 0 : 1;

while ((n = n & (n - 1)) != 0) count++;

return count;    
        
    }
};