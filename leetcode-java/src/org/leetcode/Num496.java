package org.leetcode;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

/**
 * Created by shuai on 2017/4/14.
 */
public class Num496 {
    public int[] nextGreaterElement(int[] findNums, int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        for (int num : nums){
            while (!stack.isEmpty() && stack.peek() < num){
                map.put(stack.pop(), num);
            }
            stack.push(num);
        }
        for (int i=0; i<findNums.length; i++){
            findNums[i] = map.getOrDefault(findNums[i], -1);
        }
        return findNums;
    }

    public static void main(String[] args){
        Num496 sol = new Num496();
        int[] findNums = {2,4};
        int[] nums = {1,2,3,4};
        int[] ret = sol.nextGreaterElement(findNums, nums);
        for (int x: ret){
            System.out.println(x);
        }
    }
}
