package org.leetcode;

/**
 * Created by shuai on 2017/4/11.
 */
public class Main {
    public static void main(String[] args){
        Num164 sol = new Num164();
        int[] nums = {1,1,1,1,1,5,5,5,5,5};
        int ret = sol.maximumGap(nums);
        System.out.println(ret);
    }
}
