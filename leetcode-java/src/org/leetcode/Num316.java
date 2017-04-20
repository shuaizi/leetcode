package org.leetcode;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

/**
 * Created by shuai on 2017/4/13.
 */
public class Num316 {
    public String removeDuplicateLetters(String s) {
        if (s.isEmpty()){
            return "";
        }
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i =0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(map.containsKey(ch)){
                map.put(ch, map.get(ch) + 1);
            }
            else {
                map.put(ch, 1);
            }
        }
        char ch_tmp = s.charAt(0);
        int pos_tmp = 0;
        for (int i =0; i< s.length(); i++){
            char c = s.charAt(i);
            if (c < ch_tmp){
                ch_tmp = c;
                pos_tmp = i;
            }
            if (map.get(c) == 1){
                String new_str = s.substring(pos_tmp + 1).replaceAll(
                        ch_tmp+"", "");
                return ch_tmp + this.removeDuplicateLetters(new_str);
            }
            else{
                map.put(c, map.get(c) - 1);
            }
        }
        return "";
    }

    public String removeDuplicateLetters_2(String s) {
        if (s.isEmpty()){
            return "";
        }
        int[] map = new int[26];
        Stack<Character> stack = new Stack<Character>();
        Stack<Character> ret_stack = new Stack<Character>();
        for (int i=0; i<s.length(); i++){
            char ch = s.charAt(i);
            if (stack.isEmpty()){
                stack.push(ch);
            }
            else{

            }
        }
        return "";
    }
}
