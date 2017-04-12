package org.leetcode;

/**
 * Created by shuai on 2017/4/12.
 */
public class Num164 {
    public int maximumGap(int[] nums) {
        int ret = 0;
        if (nums == null || nums.length <= 1){
            return ret;
        }
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int x : nums) {
            if (x < min) {
                min = x;
            }
            if (x > max) {
                max = x;
            }
        }
        if (max <= min){
            return ret;
        }
        int bucket_len = (max - min)/(nums.length - 1);
        if (bucket_len == 0){
            bucket_len = 1;
        }
        int[] max_tmp = new int[(max - min)/bucket_len + 1];
        int[] min_tmp = new int[(max - min)/bucket_len + 1];
        for(int i = 0; i < (max - min)/bucket_len + 1; i++){
            max_tmp[i] = Integer.MIN_VALUE;
            min_tmp[i] = Integer.MAX_VALUE;
        }
        int index;
        for(int x : nums){
            index = (x - min)/bucket_len;
            if (x < min_tmp[index]){
                min_tmp[index] = x;
            }
            if (x > max_tmp[index]){
                max_tmp[index] = x;
            }
        }
        int pre_max = max_tmp[0];
        for (int j=1; j < (max - min)/bucket_len + 1; j++){
            if (min_tmp[j] == Integer.MAX_VALUE){
                continue;
            }
            if (min_tmp[j] - pre_max > ret){
                ret = min_tmp[j] - pre_max;
            }
            pre_max = max_tmp[j];
        }
        return ret;
    }
}
