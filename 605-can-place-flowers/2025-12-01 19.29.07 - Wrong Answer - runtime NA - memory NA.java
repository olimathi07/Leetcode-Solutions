class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int c=0;
        for (int i=0;i<flowerbed.length;i++){
            if(flowerbed[i]==0) c++;
        }
        int t=c-n;
        if(t>=n) return true;
        return false;
    }
}