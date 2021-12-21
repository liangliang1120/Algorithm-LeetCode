/*

875. Koko Eating Bananas
Medium

2406

129

Add to List

Share
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
*/
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        
        if (piles == null || piles.length == 0) {
            return 0;
        }
        
        int max = piles[0];
        for (int i = 0; i < piles.length; i++) {
            if (max < piles[i]) {
                max = piles[i];
            }
        }
        
        int start = 1, end = max;
        
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if(canFinished(piles, mid) > h) {
                start = mid;
            } else {
                end = mid;
            }
        }
        
        if(canFinished(piles, start) <= h) {
            return start;
        }
        return end;
    }
    
    //return how many hour needed if koko eat eatNum per hour
    private int canFinished(int piles[], int eatNum) {
        int hour = 0;
    
        for(int i = 0; i < piles.length; i++) {
            int remainBanana = piles[i];
            if(piles[i] % eatNum == 0){
                hour += piles[i] / eatNum;
            } else{
                hour = hour + piles[i] / eatNum + 1;
            }
        }
        return hour;
    }
    
}
