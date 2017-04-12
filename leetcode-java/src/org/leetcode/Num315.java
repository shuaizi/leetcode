package org.leetcode;

import java.util.List;

/**
 * Created by shuai on 2017/4/11.
 * leetcode no.315 practice
 */
public class Num315 {
    public List<Integer> countSmaller(int[] nums) {
        return null;
    }

    protected void BottomToUpSort(int[] nums){
        int len;
        int start, mid, end;
        int i, j , k;
        int[] tmp = new int[nums.length];
        for(len = 1; len < nums.length; len *= 2){
            System.arraycopy(nums, 0, tmp, 0, nums.length);
            for(start = 0; start< nums.length; start = start + 2*len){
                mid = start + len - 1;
                end = Math.min(start + 2*len - 1, nums.length - 1);
                i = start;
                j = mid+1;
                for(k = start; k <= end; k++){
                    if(i > mid){
                        nums[k] = tmp[j++];
                    }
                    else if(j > end){
                        nums[k] = tmp[i++];
                    }
                    else if(tmp[i] <= tmp[j]){
                        nums[k] = tmp[i++];
                    }
                    else{
                        nums[k] = tmp[j++];
                    }
                }
            }
        }
    }
}

